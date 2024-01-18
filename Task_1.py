import smtplib 
import ssl 
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time

def main():

    smtp_port = 587
    smtp_server = "smtp.gmail.com"

    email_from = "samidhavaity@gmail.com"
    #email_to = "deepalibabu2008@gmail.com"

    pswd = "zxnszhgryezenbua"


    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email_from, pswd)
    print("Connected to server :-)")

    subject = "Opportunities don't happen, you create them." 

    body = """ Hello %s,
    This is my check automated mail for multiple receipents through
    python program... %s    

    This is auto gennerated mail.

    Thanks & Regards,
    Samidha Narendra Vaity
    Marvellous Infosystems
    """ 
    with open('EmailAdd.csv') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for addr, line in reader:
                msg = MIMEMultipart()
                msg['From'] = email_from
                msg['To'] = addr
                msg['Subject'] = subject
                msg.set_content(body)

            print(f"Sending email to - {name}")

            TIE_server.sendmail(email_from, name, message)
            print(f"Email sucessfully sent to - {name}")

if __name__ == "__main__":
    main()