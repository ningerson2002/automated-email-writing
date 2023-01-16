from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'johndoe@example.com'
email_password = 'password'
email_receiver = 'janedoe@example.com'

subject = 'This is the subject for my automated email'
body = """
This is the body for my automated email.

I can write on multiple lines to indicate paragraphs in my automated email.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
