import smtplib
from email.message import EmailMessage
from datetime import datetime

def send_alert():
    msg = EmailMessage()
    msg['Subject'] = "✅ Topstep Pipeline Completed"
    msg['From'] = "dr7445@outlook.com"
    msg['To'] = "dr7445@outlook.com"
    msg.set_content(f"The pipeline completed successfully at {datetime.now().isoformat()}.")

    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login("dr7445@outlook.com", "@Seagull182")
            server.send_message(msg)
        print("📧 Email alert sent.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


print("📧 Email alert sent.")
