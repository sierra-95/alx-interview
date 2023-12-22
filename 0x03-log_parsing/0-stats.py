import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        # Split the log line by space
        parts = line.split()

        # Check if the line follows the specified format
        if len(parts) >= 10:
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total file size
            total_size += file_size

            # Update status code count
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Check if 10 lines have been processed
            if line_count == 10:
                print(f"File size: {total_size}")
                for code, count in sorted(status_codes.items()):
                    if count > 0:
                        print(f"{code}: {count}")
                line_count = 0

except KeyboardInterrupt:
    # If CTRL + C is pressed, print the current stats
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")
