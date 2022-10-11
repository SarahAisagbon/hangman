# Example Project Documentation Guideline

## Milestone 1

### Creation of varibles for games using basic python commands 

- Firstly, I randomly selected a word in a list and print it.
- Next, I made a guess, checked if it was a single alphabetical character and print statements according to the outcome of the check. 

### Code Used
#randomly select a word in the list and print it
```
import random
word_list = ['passionfruit', 'mango', 'grapes', 'raspberry', 'orange']
word = random.choice(word_list)
print(word)

#make a guess and if it's a single input and in the alphabet, print good guess.

guess = input("Enter a single input: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
```

## Milestone 2

### Checking if a guessed character is in a randomly selected word

-  Firstly, I created a loop that keeps guessing until a single alphabetical input is entered.
- Then, I checked if the guess is in the randomly selected word. If so, they print one statement, and if not, another statement is printed.
- Next, I use turn the first two tasks into two different functions, where one function includes the other. I then test the function that includes the other.

### Code Used

*#Keep guessing until you enter a single alphabetical input*
```
guess = input("Enter a guess: ")  
while True:
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        guess = input("Invalid letter. Please, enter a single alphabetical character.")
```

*#Check if the guess is in the randomly selected word. If so, they print one statement, and if not, another statement is printed.*
```
guess = input("Enter a guess: ") 
if guess in word:
    print("Good guess! {} is in the word.".format(guess))
else:
    print("Sorry, {} is not in the word. Try again.".format(guess))
```

#Create a function that first converts the guess to lowercase, and then checks if the guess is in word.*
```
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess! {} is in the word.".format(guess))
        return True
    else:
        print("Sorry, {} is not in the word. Try again.".format(guess))
        return False
```
*#A function that first checks if the guess is in the word and then if it is in the word, it checks if the guess is a single alphabetical character.*
```
def ask_for_input(guess, word):
    if check_guess(guess) == True:    
        while True:
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                guess = input("Invalid letter. Please, enter a single alphabetical character.")
                check_guess(guess) == True
```

*#To test the functions, first we create a list of words and one word is randomly selected and used in the functions.*
```
if __name__ == "__main__":
    import random
    word_list = ['passionfruit', 'mango', 'grapes', 'raspberry', 'orange']
    word = random.choice(word_list)
    guess = input("Enter a guess: ")
    ask_for_input(guess, word)
```

## Milestone 3

### Create the Hangman Class

-  Firstly, I created the class and initalised the attibutes. To use the len function, I had to create a method __len__().
- Then, I created to methods - one to check if the guess is in the randomly selected word and one to check if a single alphabetical character has been inputted and if the input has already been guessed.
- Next, I use turn the first two tasks into two different functions, where one function includes the other. I then test the function that includes the other.

### Code Used
```
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
            if len(guess) != 1 or not guess.isalpha():
                guess = input("Invalid letter. Please, enter a single alphabetical character.")
            #Checks if the input has already been guessed
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            #Uses the method check guess
            else:
                self.check_guess(guess)
```

## Milestone 3

### Create the Hangman Game

- I created a function called play_game that will run all the code to run the game.
- If the player runs out of lives then the player loses. If there are more letters that need to be guessed, the game continues. Finally, if the player still has lives and all the letters have been guessed, you win the game.
- Then, I enhanced the game to allow the player to guess the word and if they guess correctly, they win the game.If they are wrong, then they lose two lives instead of one. I also changed the messages.

### Code Used
```
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