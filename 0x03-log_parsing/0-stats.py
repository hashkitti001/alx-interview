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
    """
    Print the accumulated metrics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def handle_interrupt(signum, frame):
    """
    Signal handler for keyboard interruption.
    """
    print_metrics()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, handle_interrupt)

line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        try:
            # Regex to match the log format
            match = re.match(r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$',
                    line.strip())
            if match:
                status_code = match.group(1)
                file_size = int(match.group(2))

                # Update metrics
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics()

        except Exception:
            continue

    print_metrics()

except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)