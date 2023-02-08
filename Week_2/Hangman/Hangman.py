class GuessWord:

    def __init__(self,word):
        self.word = word
        self.used_letters = [] # Helps keep track of the used letters
        self.found_letters = list("_"*len(word)) # Is used for the word display message
        self.tries = 6

    def usedLetters(self): # This method loops through the used letters list to build the
        used_list = ""     # Used letters display message
        for elem in self.used_letters:
            used_list += (str(elem)+" ")
        print("Used letters: "+used_list)

    def printWord(self): # Display the word message line
        word = "".join(self.found_letters)
        print("Word: "+word)

    def checkLetter(self):
        entry_letter = input("Guess a letter: ")
        word = self.word
        for elem in range(len(word)): # Looping through the word value to check if the entry is in the word
            if word[elem] == entry_letter:
                self.found_letters[elem] = word[elem] # Replacing the _ value in the found letters list by the current entry
        self.tries -= 1
        self.used_letters.append(entry_letter) # Adding the entry to the used letters list
    
    def checkWord(self): # This method makes a call to the other methods and displays the game info messages
        while self.tries > 0: # Keep asking for new entry unless the try value goes to 0
            print("you have "+str(self.tries)+" tries left.")
            self.usedLetters()
            self.printWord()
            self.checkLetter()
            if not "_" in self.found_letters:                   # Quits the while loop when the found letters list
                return print("You gessed the word "+self.word)  # doesn't contain _ anymore wich means that all the 
                                                                # letters in the word are found )
if __name__=='__main__':
    entry = "put a word here"
    word = GuessWord(entry)
    word.checkWord()