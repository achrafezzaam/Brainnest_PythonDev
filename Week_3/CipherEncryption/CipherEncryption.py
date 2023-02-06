class CeasarCypher:
    def __init__(self, word:str, key:int) -> None:
        self.word = word
        self.key = key
        self.cypher = self.encryption(self.word)

    def conversion(self, char:str, uplow:int, type:str) -> str:
        output = ""
        if type == "encrypt":
            output = chr((ord(char) + self.key - uplow) % 26 + uplow)
        else:
            output = chr((ord(char) - self.key - uplow) % 26 + uplow)
        return output
    
    def encryption(self, entry_word:str) -> str:
        output = ""
        for elem in entry_word:
            if elem==" ": # Check if the character is an empty space
                output+=" "
            elif (elem.isupper()): # Check if the character is uppercase
                output += self.conversion(elem,65,"encrypt")
            else:
                output += self.conversion(elem,97,"encrypt")
        return output
    
    def decryption(self) -> str:
        output = ""
        for elem in self.cypher:
            if elem==" ": # Check if the character is an empty space
                output+=" "
            elif (elem.isupper()): # Check if the character is uppercase
                output += self.conversion(elem,65,"")
            else:
                output += self.conversion(elem,97,"")
        return output

    def is_password(self, entry:str) -> bool:
        entry_cypher = self.encryption(entry)
        if entry_cypher == self.cypher:
            print("You gessed the hidden message")
            return False
        else:
            print("Wrong answer")
            return True

if __name__ == "__main__":
    string = input("Enter a string: ")
    cipher_obj_01 = CeasarCypher(string,1)
    print("The encryption of your entry is: "+cipher_obj_01.cypher)
    cipher_obj_02 = CeasarCypher("You found the hidden message",45)
    print("The encryption of the hidden message is: "+cipher_obj_02.cypher)
    x = True
    while x:
        entry = input("Try to gess the hidden message: ")
        x = cipher_obj_02.is_password(entry)
    print("Congratulations!")