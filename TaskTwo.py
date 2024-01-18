import smtplib 
from email.message import EmailMessage
import csv

def SendMail():

    smtp_port = 587
    smtp_server = "smtp.gmail.com"

    email_from = "samidhavaity@gmail.com"
    pswd = "zxnszhgryezenbua"

    subject = "We need to be willing to accept our feelings around an event in order to fully gain the benefits, which are available from it." 

    
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email_from, pswd)
    print("Connected to server :-)")

    with open('EmailAdd.csv') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for addr, line in reader:
                    msg = EmailMessage()
                    msg['From'] = email_from
                    msg['To'] = addr
                    msg['Subject'] = subject
                    msg.set_content(line)
                    TIE_server.send_message(msg)
                    print(f"Sending email to - {addr}")

    TIE_server.close()


def main():
    print("------Python Automation & Machine Learning----------")

    
    SendMail()


if __name__ == "__main__":
    main()

