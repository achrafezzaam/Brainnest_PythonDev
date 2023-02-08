class CeasarCypher:
    def __init__(self, word:str, key:int) -> None:
        self.word = word
        self.key = key # The key that will be used to encrypt the input word
        self.cypher = self.encryption(self.word)

    def conversion(self, char:str, type:str) -> str: # Encrypt or decrypt a character
        output = ""
        if ord(char) >= 97: 
            uplow = 97
        else:
            uplow = 65
        # ord() return the Unicode value of the input character
        if type == "encrypt":  
            output = chr((ord(char) + self.key - uplow) % 26 + uplow) # Will execute if the encryption method is called
        else:
            output = chr((ord(char) - self.key - uplow) % 26 + uplow) # Will execute if the decryption method is called
        if char==" ": # Check if the character is an empty space
                output = " "
        return output
    
    def encryption(self, entry_word:str) -> str:
        output = ""
        for elem in entry_word:
            output += self.conversion(elem,"encrypt")
        return output
    
    def decryption(self) -> str:
        output = ""
        for elem in self.cypher:
            output += self.conversion(elem,"")
        return output

    def is_password(self, entry:str) -> bool: # Check if the input string is equal to the object's encrypted value
        if entry == self.word:
            print("You gessed the hidden message")
            return False
        else:
            print("Wrong answer")
            return True

if __name__ == "__main__":
    string = input("Enter a string: ")
    cipher_obj_01 = CeasarCypher(string,1)
    print("The encryption of your entry is: "+cipher_obj_01.cypher)
    cipher_obj_02 = CeasarCypher("Try to find this hidden message",45) # You can change the sentence to guess here
    print("The encryption of the hidden message is: "+cipher_obj_02.cypher)
    x = True
    while x: # Keep looping until the hidden message is found
        entry = input("Try to gess the hidden message: ")
        x = cipher_obj_02.is_password(entry)
    print("Congratulations!")