# 2023-03-01 08:15:27 - ServiceA - INFO - Started processing request #123

import re
import json
from datetime import datetime
import argparse
from collections import Counter


LOG_PATTERN = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (?P<service>\w+) - (?P<level>\w+) - (?P<message>.*)'
    )

def parse_log_lines(line):
    """
    Parse a single line of the log file and return a dictionary with the extracted information
    """
    match = LOG_PATTERN.match(line)
    if match:
        return match.groupdict()
    else:
        return None

def read_logfile(filename):
    """
    Read the log file and return a list of dictionaries with the extracted information.
    """
    parser_logs = []
    malformed_lines = []
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            parsed = parse_log_lines(line.strip())
            if parsed:
                parser_logs.append(parsed)
            else:
                malformed_lines.append((line_num, line.strip()))
    return parser_logs, malformed_lines


def aggregate_logs(logs):
    """
    Aggregate logs by service and log level and most common error,
    return dictionaries for levels, service and most common error message.
    """
    level_counts = Counter()
    service_counts = Counter()
    error_messages = Counter()

    for log in logs:
        level_counts[log['level']] += 1
        service_counts[log['service']] += 1
        if log['level'] == 'ERROR':
            error_messages[log['message']] += 1
    
    most_common_error = error_messages.most_common(1)
    return level_counts, service_counts, most_common_error

def filter_logs_by_timestamp(logs, start_time, end_time):
    """
    Filter logs by timestamp range.
    """
    return [
        log for log in logs if start_time <= datetime.strptime(log['timestamp'], "%Y-%m-%d %H:%M:%S") <= end_time
    ]

def print_summary(level_counts, service_counts, most_common_error):
    """
    Print the summary of the logs.
    """
    summary = {
        "Log Levels": dict(level_counts),
        "Services": dict(service_counts),
        "Most Common Error": {
            "message": most_common_error[0][0] if most_common_error else None,
            "count": most_common_error[0][1] if most_common_error else 0
            }
    }
    print(json.dumps(summary, indent=4))


def main():
    parser = argparse.ArgumentParser(description='Log Analyzer')
    parser.add_argument("--logfile", help="Path to the log file")
    parser.add_argument("--start", help="start datetime in format YYYY-MM-DD HH:MM:SS", default=None)
    parser.add_argument("--end", help="end datetime in format YYYY-MM-DD HH:MM:SS", default=None)
    args = parser.parse_args()

    logs, malformed_lines = read_logfile(args.logfile)
    if malformed_lines:
        print(f"Malformed lines:{len(malformed_lines)}")
        for line_num, line in malformed_lines:
            print(f"Line {line_num}: {line}")
    
    if args.start and args.end:
        try:
            start_dt = datetime.strptime(args.start, "%Y-%m-%d %H:%M:%S")
            end_dt = datetime.strptime(args.end, "%Y-%m-%d %H:%M:%S")
            logs = filter_logs_by_timestamp(logs, start_dt, end_dt)
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD HH:MM:SS")
            return
    level_counts, service_counts, most_common_error = aggregate_logs(logs)
    print_summary(level_counts, service_counts, most_common_error)


if __name__ == "__main__":
    main()
