''' You work at a company that receives daily data files from external partners. These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.



The goal of this project is to automate the process of transferring the files from an external FTP server to the company's internal network.



Here are the steps you can take to automate this process:



    Use the ftplib library to connect to the external FTP server and list the files in the directory.



    Use the os library to check for the existence of a local directory where the files will be stored.



    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.



    Use the shutil library to move the files from the local directory to the internal network.



    Use the schedule library to schedule the script to run daily at a specific time.



    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. '''

from ftplib import FTP, error_perm
import shutil
from os import getcwd, mkdir
from os.path import join, exists
import schedule

def logging(text):
    with open("log_file.txt",'a') as f:
        f.write(text+"\n")

'''      Looping throw the ftp server's files and copying them localy and moving them to the 
         internal network ( the destination file for the internal network should be set in the
         internal_net variable )      '''

def files_upload():
    internal_net = "Don't know what it is but enter it here"

    '''      Connecting to the ftp server and saving the files names into a list      '''

    host = input("Write your host name then press enter: ")
    user = input("Write your username then press enter: ")
    passwd = input("Write your password then press enter: ")

    ftp = FTP(host,user,passwd)

    files_list = []

    try:
        files_list = ftp.nlst() # Getting the files
    except error_perm as resp: # Checking if the directory is empty
        logging(str(resp)) # Logging the error to the log_file


    dir_path = join(getcwd(),"file_store") # Geting the files storage directory path
    if not exists(dir_path): # Checking if the files storage directory exists
        mkdir(dir_path)      # If not the directory is created

    for file in files_list:
        try:
            local_file = join(dir_path,file)
            ftp.retrbinary(file, open(local_file, 'wb').write)
            shutil.copyfile(local_file, internal_net)
            logging(str(file)+" uploaded successfully")
        except Exception as e:
            logging(str(e))
     
    ftp.quit()
    

if __name__ == "__main__":
    files_upload()
    schedule.every().day.at("00:00").do(files_upload) # Scheduling the script to run every day at midnight
