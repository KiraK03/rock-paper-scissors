# Prompts the user to enter a value: R, P or S
#The program should convert this value into Rock, Paper, or Scissors respectively
# Asks the computer to generate a random value between 0 and 2
# Convert the computer’s choice. 0 becomes Rock; 1 becomes Paper; 2 becomes Scissors
# Compare the user’s choice with the computer’s choice to display a message indicating whether
#the user won, lost or drew against the computer
# Showcase what you have learned about conditional statements and create your own functions
import random

user = input('Enter choice(R/P/S):')
moves = range(0,3)
choice = random.choice(moves)

if user == 'R':
    print ('rock')
elif user == 'P':
    print('paper')
elif user == 'S':
    print('scissors')
else:
    print('Invalid')

if choice == 0:
    print ('rock')
elif choice == 1:
    print('paper')
elif choice == 2:
    print('scissors')
else:
    print('Invalid')



if user == choice:
    print ('tie')

elif user == 'R':
           if choice == 1:
            print('Paper wins!')
           else:
            print('Rock wins!')

elif user == 'P':
     if choice == 2:
      print('Person 2 wins!')
     else:
      print('Paper wins!')

elif user == 'S':
     if choice == 2:
      print('Person 1 wins!')
     else:
       print('Scissors wins!')

else:
    print('Other')

