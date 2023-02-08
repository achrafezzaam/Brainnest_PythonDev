import os
from os import listdir
from os.path import isfile, join
from datetime import datetime

class File: 
    def __init__(self,filename:str, directory:str) -> None: # Create the File object. This will provide the file's info
        self.filename = filename
        self.path = join(directory,self.filename)
        self.type = self.get_file_ext().strip('.')
        self.modif_time = ""

    def get_file_ext(self) -> str: # Return the file's type
        extension = os.path.splitext(self.filename)
        return extension[1]
    
    def get_file_info(self) -> datetime: # Will return the modification time of the file 
        stats = os.stat(self.path)       # ( it's also possible to return the creation time by using stats.st_ctime )
        modification_time = datetime.fromtimestamp(stats.st_mtime)
        return modification_time

    def modified_at(self, period:str) -> None: # Sets the modif_time propertie's value to the needed format
        modified_at = self.get_file_info()

        if period == "y":
            modified_at = modified_at.strftime("%Y") # Example of output: 2018
        elif period == "m":
            modified_at = modified_at.strftime("%B_%Y") # Example of output: September_1999
        else:
            modified_at = modified_at.strftime("%Y_Week%U") # ( #~# Default output #~# ) Example of output: 2023_Week03
        
        self.modif_time = modified_at
        
class FilesOrganizer:
    def __init__(self) -> None:
        self.directory = ""
        self.files_list = []
        self.period = "w"
        self.order_by = ""
        self.dir_dict = {} # This is used to move files in the appropriate directory
        self.organizer()
    
    def files_extensions_list(self) -> None: # Creates a set of files types( to avoid having duplicates ).
        output_set = set()                   # It'll be used to create directories and arange files in them
        for elem in self.files_list:
            output_set.add(elem.type)
        for elem in output_set:
            self.create_dir(elem,elem+"_files")

    def files_dates_list(self) -> None: # Creates a set of files dates ( to avoid having duplicates ).
        output_set = set()              # It'll be used to create directories and arange files in them
        for elem in self.files_list:
            elem.modified_at(self.period)
            output_set.add(elem.modif_time)
        for elem in output_set:
            self.create_dir(elem,elem+"_files")

    def create_dir(self, filename_type:str, dir_name:str) -> None: # Create a directory
        path = join(self.directory, dir_name)
        os.mkdir(path)
        self.dir_dict[filename_type] = dir_name
    
    def move_file(self, file:File) -> None: # Move the file in the appropriate directory
        if self.order_by == "ext": # Executed if the ordering is done by file type
            key = file.type
        else: # ( #~# Default option #~# ) The  ordering of the files will be done by modification time
            key = file.modif_time
        new = join(self.directory, self.dir_dict[key], file.filename)
        os.replace(file.path, new)
        
    def order_files(self) -> None: # make a call to the appropriate method depanding on the ordering method needed
        if self.order_by == "ext":
            self.files_extensions_list()
        else:
            print("You can organize your files weekly, monthly or yearly:")
            print("For yearly: enter y")
            print("For monthly: enter m")
            print("By default the files are organized by week")
            self.period = input("Your input here: ")
            self.files_dates_list()
        
        for elem in self.files_list:
            self.move_file(elem)
    
    def organizer(self) -> None:
        self.directory = input("Enter the name of the directory: ") # The name of the directory where the files to order should be saved
        os.mkdir(self.directory)
        input("Fill the ' "+self.directory+" ' with the files you want organized. Press enter when you're ready") # Will wait for the user to press enter to continue
        self.files_list = [File(f,self.directory) for f in listdir(self.directory) if isfile(join(self.directory, f))] # Creates the files objects
        print("\n########################################################################\n")
        print("Do you want to organize your files by file type or by modification date:")
        print("For type organization enter: ext")
        print("By default the files are organized by date")
        self.order_by = input("Your input here: ")
        print("\n########################################################################\n")
        self.order_files()

if __name__ == "__main__":
    FilesOrganizer()