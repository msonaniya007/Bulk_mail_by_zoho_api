# Bulk_mail_by_zoho_api
# CSV Email Sender

This Python script allows you to send emails to multiple recipients using data from a CSV file. It reads recipient details such as email address, name, subject, and message from the CSV file and sends individualized emails using Zoho Mail's SMTP server.

## Prerequisites

Before using this script, ensure you have the following:

- Python 3 installed on your system.
- A Zoho Mail account with SMTP access enabled. You'll need the email address and password of this account to send emails.
- A CSV file named recipient_details.csv containing recipient details in the following format:

    
    recipient email address, recipient name, subject, message in body
    

## Setup

1. Clone or download the repository to your local machine.

2. Install the required dependencies using pip:

    
    pip install smtplib
    

3. Open the send_emails.py file in a text editor.

4. Replace "your_zoho_email@example.com" and "your_zoho_password" with your Zoho Mail account's email address and password respectively.

## Usage

1. Place your CSV file named recipient_details.csv in the same directory as the send_emails.py script.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using the following command:

    
    python send_emails.py
    

4. The script will read the CSV file, send personalized emails to each recipient, and display a message indicating the success or failure of each email.

## Notes

- Ensure that your Zoho Mail account has SMTP access enabled. You can enable it in the Zoho Mail settings.
- Make sure your Zoho Mail account credentials are kept secure. Avoid hardcoding them directly into the script if sharing the code.
- Ensure that the CSV file is correctly formatted with the columns recipient email address, recipient name, subject, and message in body.
- The {} placeholder in the message will be replaced with the recipient's name.
- This script uses SMTP (Simple Mail Transfer Protocol) to send emails. No Zoho API key is required.

## License

This project is licensed under the MIT License - see the LICENSE file for details