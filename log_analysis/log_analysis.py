import csv
from collections import defaultdict
import re

# Function to open and read the log file
def load_log_data(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Function to extract key details from each log entry
def extract_log_details(log_entry):
    pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+).*"(?P<method>[A-Z]+) (?P<endpoint>\/\S+).*" (?P<status>\d+)'
    match = re.match(pattern, log_entry)
    if match:
        return match.group('ip'), match.group('endpoint'), match.group('status')
    return None, None, None

# Function to tally requests by IP address
def count_requests_per_ip(log_entries):
    ip_request_count = defaultdict(int)
    for entry in log_entries:
        ip, _, _ = extract_log_details(entry)
        if ip:
            ip_request_count[ip] += 1
    return ip_request_count

# Function to determine the most popular endpoint
def most_accessed_url(log_entries):
    endpoint_count = defaultdict(int)
    for entry in log_entries:
        _, endpoint, _ = extract_log_details(entry)
        if endpoint:
            endpoint_count[endpoint] += 1
    most_frequent = max(endpoint_count.items(), key=lambda x: x[1], default=(None, 0))
    return most_frequent

# Function to identify suspicious IPs (multiple failed login attempts)
def identify_suspicious_ips(log_entries, threshold=10):
    failed_attempts = defaultdict(int)
    for entry in log_entries:
        ip, _, status_code = extract_log_details(entry)
        if ip and status_code == '401':
            failed_attempts[ip] += 1
    return {ip: count for ip, count in failed_attempts.items() if count > threshold}

# Function to write results to a CSV file
def write_analysis_to_csv(ip_request_data, most_frequent_endpoint, suspicious_ips, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Record IP request counts
        writer.writerow(['IP Address', 'Request Count'])
        for ip, count in ip_request_data.items():
            writer.writerow([ip, count])

        # Record most accessed endpoint
        writer.writerow([])
        writer.writerow(['Most Accessed Endpoint'])
        writer.writerow(['Endpoint', 'Hit Count'])
        writer.writerow(most_frequent_endpoint)

        # Record suspicious IP addresses
        writer.writerow([])
        writer.writerow(['Suspicious Activity'])
        writer.writerow(['IP Address', 'Failed Login Attempts'])
        for ip, count in suspicious_ips.items():
            writer.writerow([ip, count])

# Central function to combine all processes and output results
def perform_log_analysis():
    log_file_path = r'C:\Users\jayva\OneDrive\Desktop\vrv security\log_analysis\sample.log'
 # Provide the correct log file path
    output_file_path = 'analysis_results.csv'  # Desired output CSV file

    # Read log data from file
    logs = load_log_data(log_file_path)

    # Analyze the logs for various metrics
    ip_request_data = count_requests_per_ip(logs)
    most_frequent_endpoint = most_accessed_url(logs)
    suspicious_activity = identify_suspicious_ips(logs)

    # Display results on the console
    print("IP Address           Request Count")
    for ip, count in sorted(ip_request_data.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip:<20}{count}")

    print("\nMost Accessed Endpoint:")
    print(f"{most_frequent_endpoint[0]} (Visited {most_frequent_endpoint[1]} times)")

    print("\nSuspicious Activity Detected:")
    if suspicious_activity:
        for ip, count in suspicious_activity.items():
            print(f"{ip:<20}{count}")
    else:
        print("No suspicious activity identified.")

    # Save results to CSV
    write_analysis_to_csv(ip_request_data, most_frequent_endpoint, suspicious_activity, output_file_path)
    print(f"\nAnalysis results saved to {output_file_path}")

# Main entry point for the script
if __name__ == '__main__':
    perform_log_analysis()
