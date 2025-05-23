import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load .env file
load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")

# Email content
subject = "✅ Topstep Pipeline Completed"
body = "Hello Commander Dean,\n\nYour daily pipeline has completed successfully.\n\n🧬 Token authenticated\n📂 Trades processed\n📊 Data saved to database\n\n– Ava"

# Create email message
msg = MIMEMultipart()
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECIPIENT
msg["Subject"] = subject

msg.attach(MIMEText(body, "plain"))

try:
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        print("📬 Email sent successfully!")

except Exception as e:
    print("❌ Failed to send email:", e)


