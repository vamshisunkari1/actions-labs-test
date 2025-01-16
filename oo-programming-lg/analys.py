import re

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.unique_ips = set()
        self.http_200_count = 0
        self.http_304_count = 0

    def parse_log(self):
        """Parses the log file and processes each line."""
        with open(self.log_file, 'r') as file:
            for line in file:
                self.process_line(line)

    def process_line(self, line):
        """Processes each log line to extract relevant data."""
        pattern = r'(?P<ip>\S+) - - \[(?P<timestamp>.*?)\] "(?P<request>.*?)" (?P<status>\d{3}) (?P<bytes>\d+)'
        match = re.match(pattern, line)

        if match:
            ip = match.group('ip')
            status = int(match.group('status'))

            # Track unique IPs
            self.unique_ips.add(ip)

            # Count HTTP 200 and 304 codes
            if status == 200:
                self.http_200_count += 1
            elif status == 304:
                self.http_304_count += 1

    def get_unique_ips(self):
        """Returns a list of unique IPs."""
        return sorted(self.unique_ips)

    def get_http_status_counts(self):
        """Returns counts for HTTP 200 and HTTP 304 status codes."""
        return {"HTTP 200": self.http_200_count, "HTTP 304": self.http_304_count}

# Example Usage
if __name__ == "__main__":
    log_analyzer = LogAnalyzer('nginx.log')

    # Parse the log file
    log_analyzer.parse_log()

    # Get Unique IPs
    print("\nUnique Request IPs:")
    for ip in log_analyzer.get_unique_ips():
        print(ip)

    # Get HTTP Status Counts
    print("\nCount of HTTP Status Codes:")
    status_counts = log_analyzer.get_http_status_counts()
    for status, count in status_counts.items():
        print(f"{status}: {count}")
