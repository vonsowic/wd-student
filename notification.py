u"""send notification using email"""
import smtplib
import unicodedata
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender, receiver, password, message, sub="Nowe oceny"):

    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = sub
    MESSAGE['To'] = receiver
    MESSAGE['From'] = sender
    MESSAGE.preamble = """
    Your mail reader does not support the report format.
Please visit us <a href="http://www.mysite.com">online</a>!"""

    message_as_html = MIMEText(message, 'html')
    MESSAGE.attach(message_as_html)
 
    try:
        smtp_obj = smtplib.SMTP_SSL('poczta.agh.edu.pl', 465, timeout=30)
        smtp_obj.login(sender, password)
        smtp_obj.sendmail(sender, receiver, MESSAGE.as_string())
        print("Successfully sent email")
        smtp_obj.quit()
    except smtplib.SMTPException:
        print("Error: unable to send email")


if __name__ == "__main__":
    mess = "<h1>Hello world</h1>"
    mess = unicodedata.normalize('NFKD', mess).encode('ascii', 'ignore')
    mess = mess.decode("ascii")
    send_email(
        'login@student.agh.edu.pl',
        'mail_to',
        'haslo_do_poczta.agh.edu.pl',
        mess,
        "Testowy mail")

