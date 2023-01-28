'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

class GuessWord:

    def __init__(self,word):
        self.word = word
        self.used_letters = []
        self.found_letters = list("_"*len(word))
        self.tries = 6

    def usedLetters(self):
        used_list = ""
        for elem in self.used_letters:
            used_list += (str(elem)+" ")
        print("Used letters: "+used_list)

    def printWord(self):
        word = "".join(self.found_letters)
        print("Word: "+word)

    def checkLetter(self):
        entry_letter = input("Guess a letter: ")
        word = self.word
        for elem in range(len(word)):
            if word[elem] == entry_letter:
                self.found_letters[elem] = word[elem]
        self.tries -= 1
        self.used_letters.append(entry_letter)
    
    def checkWord(self):
        while self.tries > 0:
            print("you have "+str(self.tries)+" tries left.")
            self.usedLetters()
            self.printWord()
            self.checkLetter()
            if not "_" in self.found_letters:
                return print("You gessed the word "+self.word)

if __name__=='__main__':
    entry = "put a word here"
    word = GuessWord(entry)
    word.checkWord()