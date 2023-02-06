import os
from os import listdir
from os.path import isfile, join
from datetime import datetime

class File:
    def __init__(self,filename:str, directory:str) -> None:
        self.filename = filename
        self.path = join(directory,self.filename)
        self.current_pos = join(directory, self.filename)
        self.type = self.get_file_ext().strip('.')
        self.modif_time = ""

    def get_file_ext(self) -> str:
        extension = os.path.splitext(self.filename)
        return extension[1]
    
    def get_file_info(self) -> datetime:
        stats = os.stat(self.path)
        modification_time = datetime.fromtimestamp(stats.st_mtime)
        return modification_time

    def modified_at(self, period:str) -> None:
        modified_at = self.get_file_info()

        if period == "y":
            modified_at = modified_at.strftime("%Y")
        elif period == "m":
            modified_at = modified_at.strftime("%B_%Y")
        else:
            modified_at = modified_at.strftime("%Y_Week%U")
        
        self.modif_time = modified_at
        
class FilesOrganizer:
    def __init__(self) -> None:
        self.directory = ""
        self.files_list = []
        self.period = "w"
        self.order_by = ""
        self.ext_set = []
        self.mtime_set = []
        self.dir_dict = {}
        self.organizer()
    
    def files_extensions_list(self) -> None:
        output_set = set()
        for elem in self.files_list:
            output_set.add(elem.type)
        for elem in output_set:
            self.create_dir(elem,elem+"_files")
        self.ext_set = output_set

    def files_dates_list(self) -> None:
        output_set = set()
        for elem in self.files_list:
            elem.modified_at(self.period)
            output_set.add(elem.modif_time)
        for elem in output_set:
            self.create_dir(elem,elem+"_files")
        self.mtime_set = output_set

    def create_dir(self, filename_type:str, dir_name:str) -> None:
        path = join(self.directory, dir_name)
        os.mkdir(path)
        self.dir_dict[filename_type] = dir_name
    
    def moove_file(self, file:File) -> None:
        if self.order_by == "ext":
            key = file.type
        else:
            key = file.modif_time
        new = join(self.directory, self.dir_dict[key], file.filename)
        os.replace(file.current_pos, new)
        
    def order_files(self) -> None:
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
            self.moove_file(elem)
    
    def organizer(self) -> None:
        self.directory = input("Enter the name of the directory: ")
        os.mkdir(self.directory)
        input("File the "+self.directory+" with the files you want organized. Press enter when you're ready")
        self.files_list = [File(f,self.directory) for f in listdir(self.directory) if isfile(join(self.directory, f))]
        print("\n########################################################################\n")
        print("Do you want to organize your files by file type or by modification date:")
        print("For type organization enter: ext")
        print("By default the files are organized by date")
        self.order_by = input("Your input here: ")
        print("\n########################################################################\n")
        self.order_files()

if __name__ == "__main__":
    FilesOrganizer()