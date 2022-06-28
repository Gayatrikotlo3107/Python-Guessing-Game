'''
program     : Guessing game
Author      : Gayatri kotlo
Description : guessng a number within a certain range in the fewest number of guesses.
Revisions   : 00-importing math and random module
              01-print the announcement
              02-declaring the variable nmax for the range
              03- printing the statement
              04-using randrange() for holding the secret number and assinging it to sec_num
              05- caluculating the number of guess and assinging to nGuess
              06-prints the statement
              07-while loop starts
              08-caluculate the guess by subtracting one from nGuess
              09-reads the guess from the user
              10-nested if loop with conditions
              11-prints the output using f-string
              12-when nGuess==1 prints the following statement
              13-if the user cannot guess prints the else statement






'''

import math #importing math module
import random # importing the random module
#announcement
print("Guess the secret number\n") # prints the statement
nmax=int(input("enter the maximum number in the range:"))# reads the input
print(f'Try to guess a secret number from 1 to {nmax}.\n\n')# print the statement
sec_num=random.randrange(0,nmax)# using randrange() for holding a random number
nGuess = int(math.log2(nmax)+1)  # caluculating the number of guesses
print(f'you have {nGuess} guesses available.')# prints the statement
while nGuess: #while loop
        nGuess-=1 # caluculates the nGuess
        guess=int(input("Enter your guess:"))
        if (sec_num>guess and nGuess>1): # nested if loop
            print(f'The seceret number is greater than {guess}.')#using f-string to print the statement
            print(f'you have {nGuess} guesses available.')
        elif sec_num<guess and nGuess>1:
            print(f'The seceret number is less than {guess}.')
            print(f'you have {nGuess} guesses available.')
        elif guess==sec_num:
            print(f'Correct.  well done!')
            break   # loop exists here 
        if (nGuess==1 and sec_num>guess)or (nGuess==1 and sec_num<guess):
            print(f'you have {nGuess} guess available.')
            

else:
     print(f'\n\nsorry.  No more guesses are allowed.\n The secert number was {sec_num}') # prints the statement
       

        
