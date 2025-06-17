
# Filename: app.py (or any name you prefer)

from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# --- Email Configuration ---
# Replace with your actual email details
SENDER_EMAIL = 'your_email@example.com' # Your email address
SENDER_PASSWORD = 'your_email_password' # Your email password (use app-specific password if possible)
RECIPIENT_EMAIL = 'owner_email@example.com' # The owner's email address
SMTP_SERVER = 'smtp.example.com' # Your email provider's SMTP server (e.g., smtp.gmail.com)
SMTP_PORT = 587 # Your email provider's SMTP port (usually 587 for TLS or 465 for SSL)
# ---------------------------

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        try:
            # Get form data
            full_name = request.form.get('Full Name') # Make sure the 'name' attribute in your HTML input matches this
            email_address = request.form.get('Email Address') # Make sure the 'name' attribute in your HTML input matches this
            mobile_number = request.form.get('Mobile Number') # Make sure the 'name' attribute in your HTML input matches this
            email_subject = request.form.get('Email Subject') # Make sure the 'name' attribute in your HTML input matches this
            message_content = request.form.get('Your Message') # Make sure the 'name' attribute in your HTML textarea matches this

            # Create the email content
            email_body = f"""
New message from your website contact form:

Full Name: {full_name}
Email: {email_address}
Mobile: {mobile_number}
Subject: {email_subject}

Message:
{message_content}
"""

            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = RECIPIENT_EMAIL
            msg['Subject'] = f"Website Contact: {email_subject}" # Prefix subject for easy identification

            msg.attach(MIMEText(email_body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls() # Secure the connection
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())

            # Return a success message (you might want to redirect to a thank you page)
            return "Message sent successfully!", 200

        except Exception as e:
            # Return an error message
            print(f"Error sending email: {e}")
            return "Error sending message.", 500

    # If it's not a POST request, maybe return an error or redirect
    return "Method Not Allowed", 405

if __name__ == '__main__':
    # Run the Flask app
    # In a production environment, you would use a more robust server like Gunicorn or uWSGI
    app.run(debug=True) # Set debug=False in production
