# %%
#Keep guessing until you enter a single alphabetical input 

guess = input("Enter a guess: ")  
while True:
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        guess = input("Invalid letter. Please, enter a single alphabetical character.")

# %%
#Check if the guess is in the randomly selected word. If so, they print one statement, and if not, another statement is printed.

guess = input("Enter a guess: ") 
if guess in word:
    print("Good guess! {} is in the word.".format(guess))
else:
    print("Sorry, {} is not in the word. Try again.".format(guess))

# %%

#Create a function that first converts the guess to lowercase, and then checks if the guess is in word.
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess! {} is in the word.".format(guess))
        return True
    else:
        print("Sorry, {} is not in the word. Try again.".format(guess))
        return False
        
#A function that first checks if the guess is in the word and then if it is in the word, it checks if the guess is a single alphabetical character.
def ask_for_input(guess, word):
    if check_guess(guess) == True:    
        while True:
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                guess = input("Invalid letter. Please, enter a single alphabetical character.")
                check_guess(guess) == True

#To test the functions, first we create a list of words and one word is randomly selected and used in the functions.
if __name__ == "__main__":
    import random
    word_list = ['passionfruit', 'mango', 'grapes', 'raspberry', 'orange']
    word = random.choice(word_list)
    guess = input("Enter a guess: ")
    ask_for_input(guess, word)
# %%
