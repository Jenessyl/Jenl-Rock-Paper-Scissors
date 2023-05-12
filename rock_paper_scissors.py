"""
Expert Problem: Implement the classic game "Rock-Paper-Scissors"

File Name: rock_paper_scissors.py
Name:      ?
Course:    CPTR 141
"""
import random

rand_seed = int(input('Enter a random seed: ',))
random.seed(rand_seed)

com_choice = random.randint(1, 3)
com_sym = ('')

if com_choice == 1:
    com_sym = 'Rock'

elif com_choice == 2:
    com_sym = 'Paper'

elif com_choice == 3:
    com_sym = 'Scissors'

print('The computer has chosen and so must you.\n'
      '  1) Rock\n'
      '  2) Paper\n'
      '  3) Scissors')
ply_choice = int(input('Make your choice: '))

if ply_choice > 3 or ply_choice < 1:
    print('Invalid choice. Please enter a number between 1 and 3.')
elif com_choice == ply_choice:
    print('The computer chose', com_sym, "-- it's a tie!")
elif com_choice == 1:
    if ply_choice == 2:
        print('The computer chose', com_sym, "-- you win!")
    else:
        print('The computer chose', com_sym, "-- you lose!")
elif com_choice == 2:
    if ply_choice == 3:
        print('The computer chose', com_sym, "-- you win!")
    else:
        print('The computer chose', com_sym, "-- you lose!")
elif com_choice == 3:
    if ply_choice == 1:
        print('The computer chose', com_sym, "-- you win!")
    else:
        print('The computer chose', com_sym, "-- you lose!")
