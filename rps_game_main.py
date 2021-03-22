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

##3/20/21 - Add Game Count to Scoreboard
##Add setting for NORMAL or F2E (Fight to the End)?
##Fight to the end - continue playing rounds until there is one final winner of
##each round

##Could also add a end button to wrap up the game and show the
##Rock Paper Scissors percentages for each player - Completed 3/20/21

##could also add to scoreboard # of times each option was played
##could print additional stats for players wins, losses
'''
Would need to keep a list of all options played by each user
How would that work? Potentially have a class for each player
and log all the options for each player...This is a good solution
        
'''

import random
import time

choices = ['rock','paper','scissors']

##Class and Objects the same
class Player:
    def __init__(self, name):
        self.name = name
        self.choices = []

    def add_choice(self, choice):
        self.choices.append(choice)

    def choice_cnt(self,choice):
        cnt = 0
        for c in self.choices:
            if c == choice:
                cnt+=1
        return cnt
    def message(self):
        print(self.choices)
            

    def print_stats(self, game_cnt):
        print('{} Choices'.format(self.name))
        ##Print # of times rocks used
        print('Rock: {:.0f}%'.format(((self.choice_cnt('rock')/game_cnt))*100))
        
        ##Print # of times paper used
        print('Paper: {:.0f}%'.format(((self.choice_cnt('paper')/game_cnt))*100))

        ##Print # of times scissors used
        print('Scissors: {:.0f}%'.format(((self.choice_cnt('scissors')/game_cnt))*100))

##Scoreboard class that will keep track of the score
class Scoreboard:
    ##Input when creating a class - must enter # of players
    ##Initialize # of players and their scores
    def __init__(self, players):
        self.players = players
        self.game_cnt = 0
        self.score = {}
        
        for i in range(1, (players+1)):
            self.score['Player {}'.format(str(i))] = 0
        self.score['Tie Games'] = 0
        
    def view_board(self):
        print('\nGame Count: {}'.format(self.game_cnt))
        print('\nSCORES')
        for k,v in self.score.items():
            print("{} : {}".format(k,v))
        print('\n')
      
    def add_score(self, player):
        self.score[player] +=1

    def add_game_cnt(self):
        self.game_cnt+=1

    def reset_score(self):
        for k in score.keys():
            self.score[k] = 0
            self.game_cnt = 0

    def print_res(self):
        print('Game Ended\n')
        time.sleep(2)
        for k,v in self.score.items():
            print('{} Final Score: {}, {:.0f}% of games won'.format(k, v, ((v/self.game_cnt)*100)))
        print('\n')
    def get_game_cnt(self):
        return self.game_cnt
        

##Function that returns computer choice
def com_choice(choices):
    return random.choice(choices)

##Function that compares choices
def compare(c1,c2):
    if c1 == c2:
        print('\nTie Game!\n')
        return 'Tie Games'
    if c1 == 'rock':
        if c2 == 'scissors':
            return 'Player 1'
        return 'Player 2'

    if c1 == 'paper':
        if c2 == 'rock':
            return 'Player 1'
        return 'Player 2'

    if c1 == 'scissors':
        if c2 == 'paper':
            return 'Player 1'
        return 'Player 2' 

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
        print('\nTie Game')
        scoreboard.add_score('Tie Games')
    else:
        for k, v in res_dict.items():
            if v == max_val:
                tie_cnt +=1
                winners[k] = v

        if tie_cnt == 1:
            for k in winners.keys():
                print('\n{} is the winner'.format(k))
                scoreboard.add_score(k)
        elif tie_cnt == len(list_a):
            print('\nTie Game\n')
            scoreboard.add_score('Tie Games')
        elif tie_cnt >= 2:
            ke = list(winners.keys())
            print('\nWinners')
            if len(ke) == 2:
                win_p = ' and '.join(ke)
                print('{} are the winners.'.format(win_p))

            else:
                win_p = ' , '.join(ke[:-1])
                print('{} and {} are the winners'.format(win_p,ke[-1]))

            for it in ke:
                scoreboard.add_score(it)

            time.sleep(2)
            print('These players will now battle to determine the ultimate winner.\n')
        else:
            print('Somehow your program found its way here.')
        
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
        scoreboard = Scoreboard(players)
        players_dict = {}
        players_name = []
        
        for i in range(1,players+1):
            name = 'Player {}'.format(i)
            players_name.append(name)
            players_dict[name] = Player(name)
            
        break
    else:
        print('Please enter a valid # of players.')
##Game will continue until "Quit" is entered
while True:
    ##Get Input
    p1_choice = (input('Rock, Paper, or Scissors? Type "QUIT" to quit, or END to end games: ')).lower()

    ##Ensure valid input
    if p1_choice in choices:
        
        
        c2 = com_choice(choices)
        
        ##Output
        print('\nPlayer 1 chooses {}'.format(p1_choice.capitalize()))
        print('Player 2 chooses {}'.format(c2.capitalize()))

        list_of_cho = [p1_choice, c2]

        if players > 2:
            
            addl_choices = {}
            for i in range(3,int(players+1)):
                addl_choices["c{}".format(str(i))] = com_choice(choices)
                list_of_cho.append(addl_choices["c{}".format(str(i))])    
                print('Player {} chooses {}'.format(str(i), addl_choices["c{}".format(str(i))].capitalize()))

            multi_compare(list_of_cho)
        else:

            ##Compare and Output
            results = (compare(p1_choice, c2))
            if results != 'Tie Games':
                print('\n{} wins!\n'.format(results))
            scoreboard.add_score(results)
        scoreboard.add_game_cnt()
        ##Add Player Choices
        for i in range(players):
            print(list_of_cho[i])
            players_dict[players_name[i]].add_choice(list_of_cho[i])   
        ##Display Results
        scoreboard.view_board()
        players_dict['Player 1'].message() 
    elif p1_choice == "quit":
        break
    elif p1_choice == "end":
        scoreboard.print_res()
        players_dict['Player 1'].print_stats((scoreboard.get_game_cnt()))
        print('Thanks for playing.')
        break
        
    else:
        print('Please enter a valid input.')


        




