from random import randint

def number_choice(n = 0):
    rand = randint(0,5)
    print ("the random number was " ,rand)
    sum_answer = n + rand
    print("The sum of your answer and the computer was ",sum_answer)
    return sum_answer

def win_scenario(nu, even = True):
    wingame = True
    if nu % 2 == 0 and even is True:
        return wingame
    elif nu & 2 != 0 and even is False:
        return wingame
    else:
        wingame = False
        return wingame


gameon = True
correctformat = True
while gameon:
    response = str(input("Please enter odd or even: "))
    evennum = True
    if response == "odd".lower():
        evennum = False
    elif response == "even".lower():
        pass
    else:
        print("Sorry, that input is not correct. Please try again. ")

    num = int(input("Please enter a number between 0 and 5: "))
    if (0, 5) == num:
        number_choice(num)
    if win_scenario(num, evennum) is False:
        print("Congratulations, you've won! You guessed " + response + ", and choose the number "
                                                                            ,num)
        playagain = str(input("Would you like to play again? Type 'yes' to play again. "))
        if playagain == "yes".upper():
            pass
        elif playagain == "no".islower():
            print("Thanks for playing! ")
            gameon = False
        break
    else:
        print("You lost. You guessed " + response + " and choose the number ", num)
        playagain2 = str(input("Play again? Type 'yes' to play again, and 'no' to quit."))
        if playagain2 == "yes".upper():
            gameon
        elif playagain2 == "no".islower():
            print("Thanks for playing! ")
            gameon = False
        break
