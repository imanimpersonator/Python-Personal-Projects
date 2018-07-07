from random import randint

def ropos():
    n = randint(0,2)
    answer = None
    if n == 0:
        answer = 'rock'
    elif n == 1:
        answer = 'paper'
    elif n == 2:
        answer = 'scissors'
    return answer

def win_scenario(a, b): # Where a is player and b is computer
    if a == 'rock' and b == 'scissors':
        win = True
    elif a == 'paper' and b == 'rock':
        win = True
    elif a == 'scissors' and b == 'paper':
        win = True
    elif a == b:
        win = 'draw'
    else:
        win = False

    return win

gameon = True
while gameon:

    ans = str(input('Please select rock, paper, or scissors. if you want to quit, please type "quit."\n'))

    if ans == 'quit':
        gameon = False
        break

    try:
        if win_scenario(ans,ropos()) == True:
            print('Congradulations, you chose',ans, 'and that beats',ropos())
        elif win_scenario(ans,ropos()) == False:
            print('I\'m sorry, but you lost. The computer chose', ropos(), 'and that beats', ans)
        elif win_scenario(ans, ropos()) == 'Draw':
            print('You chose',ans,'and the computer chose',ropos(),'. It s a draw!')

        again = str(input(print('play again? if you want to quit, please type "quit".\n')))
        if ans == 'quit':
            gameon = False
            break
        else:
            continue




    except ValueError:
        print('I\'m sorry, but that input is incorrect. Please select rock, paper, or scissors.')
    continue









