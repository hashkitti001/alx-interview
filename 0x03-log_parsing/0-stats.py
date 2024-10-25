#!/usr/bin/python3
'''A module to log a HTTP requests'''
import sys
import signal
import re

# Initialize variables to store metrics
total_size = 0  # Cumulative file size of all requests
status_codes = {
    "200": 0,  # Counts for each HTTP status code
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}


def print_metrics():
    """
    Prints the current metrics of the log entries processed.

    Outputs:
        - Cumulative file size across all requests.
        - Count of each HTTP status code in ascending order of the status code.
    """
    print("File size: {}".format(total_size))
    for s_code in sorted(status_codes.keys()):
        print("{}: {}".format(s_code, status_codes[s_code]))


def handle_sigint(signum, frame):
    """
    Handles the SIGINT signal (e.g., triggered by pressing Ctrl + C).
    When invoked, this function prints the current metrics
    and exits the program.

    Args:
        signum (int): The signal number.
        frame (object): The current stack frame.
    """
    print_metrics()
    sys.exit(0)


# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, handle_sigint)

line_count = 0  # Counter to track number of lines processed

try:
    for line in sys.stdin:
        """
        Reads each line from standard input, expected to be in a log format.
        Each valid line should match the following format:
        'IP - [Date] "GET /projects/260 HTTP/1.1" StatusCode FileSize'

        Example:
            127.0.0.1 - [2024-10-25] "GET /projects/260 HTTP/1.1" 200 512

        Regex groups:
            - (1) IP address: IPv4 format
            - (2) StatusCode: 3-digit HTTP status code
            - (3) FileSize: Size of the requested file in bytes

        If a line matches the format, metrics are updated:
            - Increment `total_size` by the file size.
            - Increment the count of the corresponding status code.
            - Every 10 lines, print the updated metrics.
        """
        try:
            # Define the regex pattern for log format
            input_regex = (
                r'^(\b(?:\d{1,3}\.){3}\d{1,3}\b)'  # IP Address
                r' - \[.*\]'  # Timestamp (ignored in processing)
                r' "GET /projects/260 HTTP/1\.1"'  # Fixed HTTP request
                r' (\d{3})'  # Status code
                r' (\d+)$'  # File size
            )
            match = re.match(input_regex, line)
            if match:
                line_count += 1
                status_code = match.group(2)
                file_size = int(match.group(3))

                # Update metrics
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

                # Print metrics every 10 lines
                if line_count % 10 == 0:
                    print_metrics()
        except Exception:
            # Skip lines that don't match the expected format
            continue
except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
