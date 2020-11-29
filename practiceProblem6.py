"""
 Problem Statement:-
Generate a random integer from a to b. You and your friend have to guess a number between 
two numbers a and b. a and b are inputs taken from the user. Your friend is player 1 and 
plays first. He will have to keep choosing the number and your program must tell whether 
the number is greater than the actual number or less than the actual number. Log the 
number of trials it took your friend to arrive at the number. You play the same game and 
then the person with minimum number of trials wins! Randomly generate a number after taking 
a and b as input and don’t show that to the user.

Input:
Enter the value of a

4

Enter the value of b

13

Output:
Player1 :

Please guess the number between 4 and 13

5

Wrong guess a greater number again

8

Wrong guess a smaller number again

6

Correct you took 3 trials to guess the number

Player 2:

Correct you took 7 trials to guess the number

Player 1 wins!
"""

import random

print("\nWELCOME TO THE GUESSING GAME\n")

a = int(input("Enter lower bound:"))
b =int(input("Enter upper bound:"))

player1  = 0
player2 = 0

correct1 = False
n = random.randint(a , b)
print(f"\nPlayer1 : Start guessing a number between {a} and {b}:\n")
while correct1 != True :
    player1 += 1
    numb = int(input("\nGuess a number:"))
    if numb == n :
        print(f"\nYou guessed the right number and took {player1} trials.")
        correct1 = True
    elif numb > n:
        print(f"\nYou guessed  a greater number.Try again!")
    else:
        print(f"\nYou guessed  a smaller number.Try again!")
    
correct2 = False
n1 = random.randint(a , b)
print(f"\nPlayer2 : Start guessing a number between {a} and {b}:\n")
while correct2 != True:
    player2 += 1
    guess = int(input("\nGuess a number:"))
    if guess == n1:
        print(f"\nYou guessed the right number and took {player2} trials.")
        correct2 = True
    elif guess > n1:
        print(f"\nYou guessed a greater number. Please try again!")
    else:
        print(f"\nYou entered a smaller number. Please try again!")
    
if player1 == player2:
    print(f"\nGame Tie!Both the players took {player2} trials!")
elif player1 > player2:
    print(f"\nCongratulations player2 won the game by {player1 - player2} trials.")
else:
    print(f"\nCongratulations player1 won the game by {player2 - player1} trials.")


