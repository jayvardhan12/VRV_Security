Log Analysis Project
Overview

This project is designed to process web server logs and extract valuable insights for analysis. The script focuses on counting requests per IP address, identifying the most accessed endpoints, detecting suspicious activities (like failed login attempts), and saving the results for further examination.

By utilizing Python's file handling, regular expressions, and data analysis techniques, this project provides a way to monitor server activity and identify potential security risks.

Key Features
1. Requests Per IP Address
The script counts the number of requests made by each IP address.
Results are displayed in descending order of frequency.
2. Most Accessed Endpoint
The most frequently visited endpoint (e.g., /home, /login) is identified.
The script outputs the endpoint name and the number of times it was accessed.
3. Suspicious Activity Detection
The script tracks failed login attempts (status code 401) to detect possible brute-force attacks.
It flags IP addresses that exceed a configurable threshold (default: 10 failed attempts).
4. CSV Export
All results are saved in a CSV file for further analysis or reporting.
How to Run the Project
Follow these steps to run the project on your local machine:

1. Set Up Your Environment
Make sure Python is installed on your system. You can check the installed version using:

bash
Copy code
python --version
If needed, install Python from here.

2. Clone the Repository
Clone the repository to your local machine using:

bash
Copy code
git clone https://github.com/jayvardhan12/VRV_Security.git
Then, navigate into the project folder:

bash
Copy code
cd log-analysis
3. Prepare the Log File
Ensure the log file (e.g., sample.log) is placed in the project directory. This log file should be in the Common Log Format (CLF) or a similar format.

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
No external libraries required, uses Python's built-in libraries: re, csv, collections.
License
This project is open-source and available under the MIT License.
