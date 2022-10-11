#%%  
from lib2to3.pytree import LeafPattern
from mimetypes import guess_all_extensions
import random

class Hangman:
    #initalise attributes 
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        #word_guessed is a list of ' '
        self.word_guessed = [" " for i in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    #To use the len function, I need to create a method __len__()
    def __len__(self):
        return len(self.word_list)
    
    # A method check_guess with guess as it's parameter
    def check_guess(self, guess):
        #Convert the guess to lowercase
        guess = guess.lower()
        #If guess is in the word, print a statement and replace '' with the guess in the list word_guessed
        if guess in self.word:
            print("Good guess! {} is in the word.".format(guess))
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
        #reduce the number of letters that still need to be guessed by 1
            self.num_letters -= 1
        #if the guess is wrong, a life is lost and two statements are printed
        else:
            self.num_lives -= 1
            print("Sorry, {} is not in the word.".format(guess))
            print("You have {} lives left.".format(self.num_lives))
        
        #add guess to the list of guesses
        self.list_of_guesses.append(guess)
    
    #A method ask for input that first checks if a single alphabetical character has been inputted.  
    def ask_for_input(self):
        while True:
            guess = input("Enter a guess: ")
            if len(guess) != 1 and guess == self.word:
                self.num_letters = 0
                print("Congratulations! You guessed the word correctly!")
                break
            
            elif len(guess) != 1 and guess != self.word:
                self.num_lives -= 2
                if self.num_lives <= 0:
                    break
                
                else:
                    print("Sorry, {} is not the word.".format(guess))
                    print("You have {} lives left.".format(self.num_lives))
                
            elif len(guess) != 1 or not guess.isalpha():
                guess = input("The guess should be a single alphabetical character unless you think you know the word. Please, enter a valid guess.")
            #Checks if the input has already been guessed
            elif guess in self.list_of_guesses:
                print("You already tried that letter! Here is a reminder of the all your guesses so far: {} \n Please try again!".format(self.list_of_guesses))
            #Uses the method check guess
            else:
                self.check_guess(guess)
                break
            
#create a function called play_game that will run all the code to run the game. 
def play_game():
    game = Hangman(word_list, num_lives = 5)
    while True:
        #If the player runs out of lives then one statement is printed. 
        if game.num_lives <= 1:
            print("Unfortunately, you have no more lives. You lost!")
            break
        #If there are more letters that need to be guessed, the game continues. 
        elif game.num_letters > 0:
            game.ask_for_input()
        #Finally, if the player still has lives and all the letters have been guessed, you win the game. 
        else:
            print("Congratulations, you win! You only made {} incorrect guesses.".format(5-game.num_lives))
            break
        
if __name__ == "__main__":
    word_list = ['passionfruit', 'mango', 'grapes', 'raspberry', 'orange']
    play_game()
# %%
