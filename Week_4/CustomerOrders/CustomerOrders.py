import re
from datetime import datetime

class InputVerification:
    def __init__(self, entry) -> None:
        self.entry_text = entry
        
    def is_email(self): # This method check if the object has an email format
        pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")
        if pattern.search(self.entry_text):
            return True

    def is_valid_date(self): # This method return True if the object is valid date format days between 1 and 31, months 1 and 12 and year doesn't current year
        x = re.split("[\-\/]",self.entry_text)
        year = datetime.now().year
        if (int(x[0])>0 and int(x[0])<=31) and (int(x[1])>0 and int(x[1])<=12) and int(x[2])<=year:
            return True

    def is_date_format(self): # This method check if the object has a date format ( dd-mm-yyyy or dd/mm/yyyy )
        pattern = re.compile("^[0-9]{1,2}[\-\/][0-9]{1,2}[\-\/][0-9]{4}$")
        if pattern.search(self.entry_text):
            return self.is_valid_date(self.entry_text)

class Order():
    def __init__(self, order_info, **kwargs) -> None:
        self.order_info = order_info
        self.info_type = {"Order Number":"order_id","Customer":"Custumer_name","Items":"Item_name"}
        self.data = {}
        for key,value in kwargs.items():
            self.info_type[key] = value
        self.get_info()
        self.format_items()
        self.__repr__()

    def get_info(self): # ex: [order_id]125[order_id] the value of x[1] will be 125
        for key in self.info_type:
            split_info = "\["+self.info_type[key]+"\]"
            x = re.split(split_info,self.order_info)
            self.data[key] = x[1]
    
    def format_items(self): # Format the items data into a dictionnary.
        items_dict = {}
        items = self.data["Items"]
        items_list = re.split("\,",items)
        for elem in items_list:
            x = re.split("\:",elem)
            if len(x)>1:
                items_dict[x[0]] = int(x[1])
            else:
                items_dict[x[0]] = 1
        self.data["Items"] = items_dict
    
    def __repr__(self) -> str:
        print("The order's information is as follows:\n"+str(self.data)+"\n")
    

if __name__ == "__main__":
    with open("data.txt","rt") as f:
        for line in f:
            if line.startswith("Order"):
                x = Order(line) #,id="order_id",customer="Custumer_name",item="Item_name"