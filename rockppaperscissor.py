"""
Implements the game of Rock-Paper-Scissors!

The Game:
Each player choses a move (simultaneously) from the choices:
rock, paper or scissors. 
If they chose the same move the game is a tie. Otherwise:
rock beats scissors
scissors beats paper
paper beats rock.

In this program a human plays against an AI. The AI choses randomly
(we promise). The game is repeated N_GAMES times and the human gets
a total score. Each win is worth +1 points, each loss is worth -1
"""
import random

N_GAMES = 3

def main():
    score=0
    print_welcome()
    for i in range(N_GAMES):
        human_move=get_human_move()
        ai_move=get_ai_move()
        print("AI choose move:",ai_move)
        winner=get_winner(human_move,ai_move)
        score=get_scores(winner,score)
        print("winner is",winner)
        print()
    print("Total score is",score)

def print_welcome():
    print('Welcome to Rock Paper Scissors')
    print('You will play '+str(N_GAMES)+' games against the AI')
    print("Notes:")
    print('1.rock beats scissors')
    print('2.scissors beats paper')
    print('3.paper beats rock')
    print('4.please enter the input in lowercase')
    print('----------------------------------------------')
    print('')

def get_human_move():
    print("please choose your move: rock, paper or scissor")
    ask_user=input("Enter your move: ")
    test=1
    while test>0:
        if ask_user=='rock' or ask_user=='paper' or ask_user=='scissor':
            return ask_user
            test=-1
        else:
            ask_user=input("please enter valid input: ")

def get_ai_move():
    """
    for now the AI plays randomly. But the optimal strategy is:
    If you lose, switch to the thing that beats the thing your opponent just played. 
    If you win, switch to the thing that would beat the thing that you just played.
    """
    random_choose=random.randint(1,3)

    if random_choose==1:
        return 'rock'
    elif random_choose==2:
        return 'paper'
    elif random_choose==3:
        return 'scissor'

def get_winner(human_move,ai_move):
    if human_move==ai_move:
        return 'Tie'
    if human_move=='rock':
        if ai_move=='scissor':
            return 'Human'
        return 'AI'
    if human_move=='paper':
        if  ai_move=='rock':
            return 'Human'
        return 'AI'
    if human_move=='scissor':
        if ai_move=='paper':
            return 'Human'
        return 'AI'

def get_scores(winner,score):
    if winner=='AI':
        score-=1
    elif winner=='Human':
        score+=1
    elif winner=='Tie':
        score+=0
    return score
if __name__ == '__main__':
    main()
