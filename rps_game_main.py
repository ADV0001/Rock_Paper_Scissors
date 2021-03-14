##Rock, Paper, Scissors Game to post on Github
##Plan is to post several versions until the most
##efficient code is found

##Python game that plays rock, paper, scissors with a computer
##User inputs their choice, computer shows their choice, result
##is shown

import random

choices = ['rock','paper','scissors']


##Function that returns computer choice
def com_choice(choices):
    return random.choice(choices)

##Function that compares choices
def compare(c1,c2):
    if c1 == c2:
        return 'Tie Game, Play Again!'
    if c1 == 'rock':
        if c2 == 'scissors':
            return 'Player 1 Wins!'
        return 'Player 2 Wins!'

    if c1 == 'paper':
        if c2 == 'rock':
            return 'Player 1 Wins!'
        return 'Player 2 Wins!'

    if c1 == 'scissors':
        if c2 == 'paper':
            return 'Player 1 Wins!'
        return 'Player 2 Wins' 

##Get Input
p1_choice = (input('Rock, Paper, or Scissors? ')).lower()

##Compare

##Ensure valid input
if p1_choice in choices:
    c2 = com_choice(choices)

    ##Output
    print('Player 1 chooses {}'.format(p1_choice.capitalize()))
    print('Player 2 chooses {}'.format(c2.capitalize()))
    print(compare(p1_choice, c2))
    
else:
    print('Please enter a valid input.')
    




