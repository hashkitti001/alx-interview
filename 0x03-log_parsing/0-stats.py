#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables to store metrics
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}


def print_metrics():
    '''Prints metrics from a stream of server request logs'''
    print(f"File size: {total_size}")
    for s_code in sorted(status_codes.keys()):
        print(f"{s_code}: {status_codes[s_code]}")


def handle_sigint(signum, frame):
    """Handles the SIGINT signal when Ctrl + C is pressed"""
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_sigint)

line_count = 0
try:
    for line in sys.stdin:
        try:
            input_regex = (
                r'^(\b(?:\d{1,3}\.){3}\d{1,3}\b)'
                r' - \[.*\]'
                r' "GET /projects/260 HTTP/1\.1"'
                r' (\d{3})'
                r' (\d+)$'
            )
            match = re.match(input_regex, line)
            if match:
                line_count += 1
                status_code = match.group(2)
                file_size = int(match.group(3))
                # Update metrics
                total_size += file_size
                status_codes[status_code] += 1

                if line_count % 10 == 0:
                    # Print details after 10 rounds
                    print_metrics()
        except Exception:
            # Skip any invalid input
            continue
except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
