''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.



Here are the steps you can take to automate this process:



    Use the smtplib library to connect to the email server and send the emails.



    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.



    Use the os library to access the report files that need to be sent.



    Use a for loop to iterate through the list of recipients and send the email and attachment.



    Use the schedule library to schedule the script to run daily at a specific time.



    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

import smtplib, ssl
import os
from os import getcwd,listdir
from os.path import isfile, join
import schedule

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def loging(text):
    with open("log_file.txt",'a') as f:
        f.write(text+"\n")

'''      Sending a mail with an attachment to it      '''

def send_mail(mail_recipiant,message,attachment_link):
    subject = "Daily report"
    sender_email = input("Type your email and press enter: ")
    password = input("Type your password and press enter: ")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = mail_recipiant
    message["Subject"] = subject
    message["Bcc"] = mail_recipiant

    message.attach(MIMEText(message, "plain"))

    filename = attachment_link

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)
    text = message.as_string()
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, mail_recipiant, text)
            loging("Mail sent successfully")
        except Exception as e:
            loging(e)
        finally:
            server.quit()

'''      Getting all the reports in the report_files directory and sending a mail for each one      '''

def check_reports():
    dir_path = join(getcwd(),"report_files")

    files_list = [file for file in listdir(dir_path) if isfile(join(dir_path,file))]
    for file in files_list:
        with open(join(dir_path,file), 'r') as f:
            content = f.readlines()
            recipient_mail = content[0]
            mail_attachement = content[1]
            mail_content = content[2]
            send_mail(recipient_mail,mail_content,mail_attachement)
            f.close()
        os.remove(file)

if __name__=="__main__":
    check_reports()
    '''      Sheduling the daily script execution at 00:00      '''
    schedule.every().day.at("00:00").do(check_reports)