import random

print('---------------------------')
print('    Rock Paper Scissors')
print('---------------------------')
print('1) ✊ Rock')
print('2) ✋ Paper')
print('3) ✌️  Scissors')
player = int(input('Pick a number!:  '))
computer = random.randint(1, 3)
choices = {1: '✊ Rock', 2: '✋ Paper', 3: '✌️  Scissors'}

if player not in choices:
    print('Invalid input')
else:
    print('You chose', choices[player])
    print('Computer chose', choices[computer])


if player == 1 and computer == 3:
    print('Player wins!')
elif computer == 1 and player == 3:
    print('Computer wins!')
elif player == 2 and computer == 1:
    print('Player wins!')
elif computer == 2 and player == 1:
    print('Computer wins!')
elif player == 3 and computer == 2:
    print('Player wins!')
elif computer == 3 and player == 2:
    print('Computer wins!')
elif player == computer:
    print('Tie!')


