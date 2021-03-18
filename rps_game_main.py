##Rock, Paper, Scissors Game to post on Github
##Plan is to post several versions until the most
##efficient code is found

##Python game that plays rock, paper, scissors with a computer
##User inputs their choice, computer shows their choice, result
##is shown


##New Feature - Add Scoreboard to keep count of results 1.1
##New Feature - Add multiple computers/players
##3/17/21 - Continue working on multiple player features
    ##Ideas to keep in mind, - Only time tie will score is if all players,
    ## enter the same answer, otherwise must a break tie-breaker - Complete 3/19/21
    ## Could Also be a tie if everybody beats everybody

import random
import time

choices = ['rock','paper','scissors']

##Should be able to create a scoreboard class to keep score
##of the RPS games. Should feed the scoreboard class the number
##of players and keep track of score
'''
Methods that could be used for the scoreboard
-Display Score
-Reset Score

'''
class Scoreboard:
    def __init__

##Function that returns computer choice
def com_choice(choices):
    return random.choice(choices)

##Function that compares choices
def compare(c1,c2):
    if c1 == c2:
        return 'Tie Game, Play Again!\n'
    if c1 == 'rock':
        if c2 == 'scissors':
            return 'Player 1 Wins!\n'
        return 'Player 2 Wins!\n'

    if c1 == 'paper':
        if c2 == 'rock':
            return 'Player 1 Wins!\n'
        return 'Player 2 Wins!\n'

    if c1 == 'scissors':
        if c2 == 'paper':
            return 'Player 1 Wins!\n'
        return 'Player 2 Wins\n' 

def compare_rev(c1,c2):
    if c1 == c2:
        return 'Tie'
    if c1 == 'rock':
        if c2 == 'scissors':
            return '1'
        return '2'

    if c1 == 'paper':
        if c2 == 'rock':
            return '1'
        return '2'

    if c1 == 'scissors':
        if c2 == 'paper':
            return '1'
        return '2'

def list_compare(val, idx, list_a):
    win_count = 0
    for i in range(len(list_a)):
        if i!=idx:
           if compare_rev(val, list_a[i]) == '1':
               win_count+=1
    return win_count

##Potential Better Multi Player Compare Function
def multi_compare(list_a):
    tie_cnt = 0
    res_dict = {}
    res_list = []
    winners = {}
    cur = list_a[0]
    for i in range(0,len(list_a)):
        res_dict['Player {}'.format(i+1)] = (list_compare(list_a[i],i,list_a))
        res_list.append(list_compare(list_a[i],i,list_a))

    max_val = max(res_list)
    max_index = res_list.index(max_val)
    if max_val == 0:
        print('Tie Game')
    else:
        for k, v in res_dict.items():
            if v == max_val:
                tie_cnt +=1
                winners[k] = v

        if tie_cnt == 1:
            for k in winners.keys():
                print('\n{} is the winner'.format(k))
        elif tie_cnt == len(list_a):
            print('\nTie Game\n')
        elif tie_cnt == 2:
            ke = list(winners.keys())
            print('\nWinners')
            if len(ke) == 2:
                win_p = ' and '.join(ke)
                print('{} are the winners.'.format(win_p))
            else:
                win_p = ' , '.join(ke[:-1])
                print('{} and {} are the winners'.format(win_p,ke[-1]))

            time.sleep(2)
            print('These players will now battle to determine the ultimate winner.\n')
        else:
            pass
        
##
##        else:
##            print('Error in Multi Compare')
        
            
        
##Counters
p1_score = 0
p2_score = 0
tie_score = 0
game_count=0

##Welcome Screen
while True:
    print('WELCOME TO ROCK PAPER SCISSORS - HOW MANY PLAYERS WOULD YOU LIKE TO PLAY WITH? (MAX 4 PLAYERS)')
    players = int(input())
    if ((players <= 4) and (players >= 2)):
        break
    else:
        print('Please enter a valid # of players.')
##Game will continue until "Quit" is entered
while True:
    ##Get Input
    p1_choice = (input('Rock, Paper, or Scissors? Type "QUIT" to quit: ')).lower()

    ##Ensure valid input
    if p1_choice in choices:
        c2 = com_choice(choices)
        
        ##Output
        print('\nPlayer 1 chooses {}'.format(p1_choice.capitalize()))
        print('Player 2 chooses {}'.format(c2.capitalize()))

        if players > 2:
            list_of_cho = [p1_choice, c2]
            addl_choices = {}
            for i in range(3,int(players+1)):
                addl_choices["c{}".format(str(i))] = com_choice(choices)
                list_of_cho.append(addl_choices["c{}".format(str(i))])    
                print('Player {} chooses {}'.format(str(i), addl_choices["c{}".format(str(i))].capitalize()))

            multi_compare(list_of_cho)
        else:
            ##Compare and Output
            results = (compare(p1_choice, c2))
            print(results)
            ##Display Results
            game_count+=1
            if results == 'Player 1 Wins!\n':
                p1_score+=1
            elif results == 'Player 2 Wins!\n':
                p2_score+=1
            else:
                tie_score+=1
            print('Game Count: {}'.format(game_count))
            print("Player 1 Score: {} Player 2 Score: {} Tie Games: {}\n".format(p1_score,p2_score,tie_score))
            
    elif p1_choice == "quit":
        break
    else:
        print('Please enter a valid input.')


        




