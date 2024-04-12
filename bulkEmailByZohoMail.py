import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# Function to send email using Zoho Mail
def send_email(sender_email, sender_password, recipient_email, recipient_name, subject, message):
    try:
        # Connect to Zoho Mail's SMTP server
        server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
        server.ehlo()
        # Login to your Zoho Mail account
        server.login(sender_email, sender_password)

        # Create message container
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add recipient's name in the email body
        message_with_name = message.format(recipient_name)

        # Attach message to email body
        msg.attach(MIMEText(message_with_name, 'plain'))

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        print(f"Email sent to {recipient_email}")

        # Close the connection
        server.quit()

    except Exception as e:
        print(f"Error: {e}")

# Main function to read CSV file and send emails
def main():
    # Zoho Mail account credentials
    sender_email = "your_zoho_email@example.com"
    sender_password = "your_zoho_password"

    # Path to the CSV file
    csv_file = "recipient_details.csv"

    # Read CSV file and send emails
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            recipient_email = row['recipient email address']
            recipient_name = row['recipient name']
            subject = row['subject']
            message = row['message in body']
            
            # Send email for each record
            send_email(sender_email, sender_password, recipient_email, recipient_name, subject, message)

if _name_ == "_main_":
    main()