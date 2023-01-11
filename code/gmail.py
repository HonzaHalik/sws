from email.message import EmailMessage
import ssl
import smtplib
import os

def send_email(email_user, email_password, email_reciever, subject, body):
    em = EmailMessage()
    em["From"] =  email_user
    em["To"] = email_reciever
    em["subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
        smtp.login(email_user, email_password)
        smtp.sendmail(email_user, email_reciever, em.as_string())
    print("email sent")

send_email(email_user='jan.halik.dev@gmail.com', email_password='zdomxaomlnpshxvs', email_reciever='recipient@example.com', subject='Hello', body='Hello, world!')
