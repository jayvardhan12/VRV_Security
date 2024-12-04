Log Analysis Project
Overview
This project processes web server logs to extract valuable insights for analysis. The script counts requests per IP address, identifies the most accessed endpoints, detects suspicious activities such as failed login attempts, and saves the results for further examination.

By utilizing Python's file handling, regular expressions, and data analysis techniques, this project provides an effective way to monitor server activity and identify potential security risks.

Key Features
Requests Per IP Address:

The script counts the number of requests made by each IP address.
Displays results in descending order of frequency.
Most Accessed Endpoint:

Identifies the most frequently visited endpoint (e.g., /home, /login).
Outputs the endpoint name and the number of times it was accessed.
Suspicious Activity Detection:

Tracks failed login attempts (HTTP status code 401) to detect potential brute-force attacks.
Flags IP addresses that exceed a configurable threshold (default: 10 failed attempts).
CSV Export:

Saves all analysis results into a CSV file for further review or reporting.
How to Run the Project
Follow these steps to run the project on your local machine:

1. Set Up Your Environment
Ensure Python is installed on your system. You can verify the installation by running:

bash
Copy code
python --version
If Python is not installed, download and install it from here.

2. Clone the Repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/jayvardhan12/VRV_Security.git
Navigate into the project folder:

bash
Copy code
cd VRV_Security/log-analysis
3. Prepare the Log File
Make sure the log file (e.g., sample.log) is placed in the project directory. The log file should be in a Common Log Format (CLF) or a similar format.

4. Run the Script
Execute the Python script by running:

bash
Copy code
python log_analysis.py
5. View the Results
The script will output results in the terminal and generate a CSV file (log_analysis_results.csv) with the following data:

IP address request counts
Most accessed endpoint
Suspicious IP activity
Example Terminal Output:
yaml
Copy code
IP Address           Request Count
203.0.113.5          8
198.51.100.23        8
192.168.1.1          7
10.0.0.2             6
192.168.1.100        5

Most Accessed Endpoint:
/login (Accessed 13 times)

Suspicious Activity Detected:
No suspicious activity detected.

Results saved to log_analysis_results.csv.
Example CSV Output (log_analysis_results.csv):
csv
Copy code
IP Address,Request Count
203.0.113.5,8
198.51.100.23,8
192.168.1.1,7
10.0.0.2,6
192.168.1.100,5

Most Frequently Accessed Endpoint
Endpoint,Access Count
/login,13

Suspicious Activity
IP Address,Failed Login Count
Customization
Failed login threshold: You can adjust the threshold for suspicious activity detection by modifying the default value (10) in the script.
Log file format: The script is designed to work with logs in a standard format. If your logs differ, you may need to update the regular expression pattern in the extract_log_details function.
Dependencies
Python 3.x
No external libraries are required; the script uses Python's built-in libraries:

re (for regular expressions)
csv (for reading/writing CSV files)
collections (for counting IP addresses and endpoints)
License
This project is open-source and available under the MIT License.

