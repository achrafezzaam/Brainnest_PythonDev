''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.



Here are the steps you can take to automate this process:



    Use the smtplib library to connect to the email server and send the emails.



    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.



    Use the os library to access the report files that need to be sent.



    Use a for loop to iterate through the list of recipients and send the email and attachment.



    Use the schedule library to schedule the script to run daily at a specific time.



    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

from smtplib import SMTP
from os import getcwd,listdir
from os.path import isfile, join
import schedule

def send_mail():
    pass

dir_path = join(getcwd(),"report_files")
files_list = [file for file in listdir(dir_path) if isfile(join(dir_path,file))]
for file in files_list:
    with open(join(dir_path,file), 'r') as f:
        content = f.readlines()
        recipient_mail = content[0]
        mail_attachement = content[1]
        mail_content = content[2]
        send_mail(recipient_mail,mail_attachement,mail_content)
        f.close()

# mail_sender = "achraf.ezzaam@gmail.com"
# mail_receiver = "achraf.ezzaam@gmail.com"
# message = "Mail test messages!!!"
# password = input(str("Please enter your email's password: "))

# with SMTP('smtp.gmail.com',587) as server:
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
    
#     server.login(mail_sender,password)
#     print("Login successfully")

#     server.sendmail(mail_sender,mail_receiver,message)
#     print("Email has been sent to: "+mail_receiver)

'''      Sheduling the daily script execution at 00:00      '''

# schedule.every().day.at("00:00").do()    

'''      Log file for tracking the sent mail status      '''


