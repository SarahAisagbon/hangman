#%%
#randomly select a word in the list and print it
import random
word_list = ['passionfruit', 'mango', 'grapes', 'raspberry', 'orange']
#randomly select a word in a list
word = random.choice(word_list)
#print the word
print(word)

# %%
#make a guess and if it's a single input and in the alphabet, print good guess.
guess = input("Enter a single input: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

