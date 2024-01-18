import smtplib 
from email.message import EmailMessage
import csv
import datetime

def sendEmail():
    smtp_port = 587
    smtp_server = "smtp.gmail.com"

    email_from = "samidhavaity@gmail.com"
    pswd = "zxnszhgryezenbua"
    subject = "Auto Genearated testing mail"

    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email_from, pswd)
    print("Connected to server :-)")

    
    today = datetime.datetime.now().strftime("%d-%m")
    yearnow = datetime.datetime.now().strftime("%Y")
    writeInd = []
    with open('Bday.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for rows in reader:        
            bday = reader.strftime("%d-%m")
            if(today == bday) and yearnow not in str(item['Year']):                          
                for Email, Dialogue in reader:
                    msg = EmailMessage()
                    msg['From'] = email_from
                    msg['To'] = Email
                    msg['Subject'] = subject
                    msg.set_content(Dialogue)
                    TIE_server.send_message(msg)
                    print(f"Sending email to - {addr}")
                    writeInd.append(index)

        
        #for i in writeInd:
            #yr = df.loc[i, 'Year']
            #df.loc[i, 'Year'] = str(yr) +','+ str(yearnow)
            
        TIE_server.close()

def main():
    print("------Python Automation & Machine Learning----------")

    
    sendEmail()   
   

if __name__=="__main__":
    main()



    
