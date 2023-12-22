from collections import defaultdict
import sys

def print_statistics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def process_logs():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            # Check if the line follows the specified format
            if len(parts) >= 9 and parts[3].startswith("GET") and parts[8].isdigit():
                status_code = parts[8]
                file_size = int(parts[-1])

                # Update total file size
                total_size += file_size

                # Update status code count
                if status_code in {"200", "301", "400", "401", "403", "404", "405", "500"}:
                    status_codes[status_code] += 1

                line_count += 1

                # Check if 10 lines have been processed
                if line_count == 10:
                    print_statistics(total_size, status_codes)
                    line_count = 0

    except KeyboardInterrupt:
        # If CTRL + C is pressed, print the current stats
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    process_logs()
