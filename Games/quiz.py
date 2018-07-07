# add pictures with countries

with open('countries.txt') as f:
    words = [word.strip() for word in f]


def guessed(answer, anslist):
    anslist.append(answer)
    print(anslist)
    print('number of correct answers is', len(anslist)) # try sorting list alphabetically


guesslist = []
lives = round(len(words) / 5)

gameOn = True

while gameOn:
    print('You have',lives,'live(s).')
    ans = input("Guess a country")
    if ans in words:
        print('yes,', ans, 'is a country. It is now removed from the deck.\n')
        print('Below is a list of correct answers')
        words.remove(ans)

        guessed(ans, guesslist)

        if not words:
            print('congraduations, there are no more questions. You won!')
            f.close()
            break

    elif ans == 'quit':
        print('Thank you for playing!')
        gameOn = False
        f.close()

    else:
        print("sorry, ", ans, "is either not a country, or not in the list. Please try again.")
        lives -= 1

        if lives <= 0:
            print('Ran out of lives. try again next time.')
            break


