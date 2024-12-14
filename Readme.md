# PROJECT 1 : Weather Fetcher and Updater

## Project Description
This project is a Python script that fetches real-time weather data for multiple locations and updates the information every 120 seconds. It is ideal for users who want to monitor weather conditions across various cities in real-time.

## KEY FEATURES 
- Fetches current weather details for user-specified locations.
- Displays:
  - Temperature
  - Feels Like Temperature
  - Weather Description
  - Humidity
  - Wind Speed
- Updates weather details every 120 seconds automatically.
- User-friendly input to specify desired cities.
- Lightweight and efficient design, making it suitable for beginners and advanced users alike.

## HOW TO USE
1. Run the script.
2. Enter the locations you want to monitor when prompted.
3. The script will fetch and display weather details for the specified cities.
4. The information will refresh every 120 seconds.

## TOOLS I USED
- Python
- Replit (for development) 
- Weather API (I used OpenWeatherApi)







# PROJECT 2 : Email Automation Tool

## 📜 OVERVIEW
The Email Automation Tool is a Python-based application designed to automate the process of sending emails. It can send personalized emails to multiple recipients, handle attachments, and support scheduling. This tool is ideal for businesses, freelancers, or anyone looking to save time on repetitive email tasks.

## 🚀 FEATURES
Bulk Email Sending: Send emails to multiple recipients simultaneously.
Personalization: Customize the subject and body of emails for each recipient using data from a CSV file.
Attachments: Attach files (PDFs, images, etc.) to your emails.
Error Handling: Logs failed email attempts for review.
HTML Support: Send visually appealing HTML-based emails.
Scheduling: Automate emails to be sent at specific times (optional).

## 🛠️ TECHNOLOGIES USED
Python: Core programming language.
smtplib: Library i used for sending emails via SMTP.
email.mime: Library used for creating and formatting email content.
pandas: Library for handling recipient data from CSV files.
schedule: For scheduling emails.

## 📂 PROJECT STRUCTURE
email-automation-tool/  
│  
├── recipients.csv          # Sample dataset with recipient details  
├── main.py                 # Core script for sending emails  
├── templates/              # Folder for HTML email templates (optional)  
├── logs/                   # Folder for storing logs of sent/failed emails  
└── README.md               # Project documentation  

## ⚙️ SETUP INSTRUCTIONS
1. Clone the Repository
Run the following code to clone this repository:

git clone https://github.com/Onoruoiza514/email-automation-tool.git  
cd email-automation-tool  

2. Install Dependencies by running the following line:

pip install pandas schedule yagmail  

3. Prepare the CSV Fil
Update recipients.csv with your recipient details. Ensure the following columns:

Name: Recipient’s name.
Email: Recipient’s email address.
Subject: Email subject.
Message: Email body.

## 🖥️ USAGE
1. Run the Script
Execute the script to send emails:

python main.py  

3. Optional Features
Add Attachments: Place files in the /attachments/ folder and reference them in the script.
Schedule Emails: Use the schedule library to send emails at specific times.

## 🔐 SECURITY NOTE
Use environment variables to store sensitive information like your email credentials.
Never hard-code passwords in the script.

## 📈 FUTURE ENHANCEMENTS
Add OAuth2 authentication for Gmail/Outlook.
Build a user-friendly GUI.
Add multi-language support.

## 🤝 Contributing ????
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

📧 Contact
For questions or feedback, reach out at:

Email: abdulfaatihitijani@gmail.com
GitHub: Onoruoiza514
