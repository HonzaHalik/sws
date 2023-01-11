import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg['Subject'] = 'test subject'
msg['From'] = 'J. B. Goode <halik.honza.dev@gmail.com>'
msg['To'] = 'Pump King <halik.honza2@gmail.com>'

msg.set_content("""Hello World,
    I am writing to tell you that I am alive!

Yours very truly,
Johnny B. Goode
""")

smtp = smtplib.SMTP('localhost:8025')

smtp.send_message(msg)

smtp.quit()

print(msg)