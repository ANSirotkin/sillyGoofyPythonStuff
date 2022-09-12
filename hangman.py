#hangman (the game)
#hangman:
#  _______^
#  |      |
#  {}      |
# {}{}{}     |
# {} {}     |
#         |
#        /-\

#take the word to be guessed
def start():
    print('Welcome to Hangman!!!!! :)')
    word = input('Please type the word to be guessed: ')
    word = word.upper()
    print('\n\n\n\n\n\n\n\n\n')
    rword = ''
    for x in range(len(word) - 1):
        rword += '_ '
    rword += '_'
    return word, rword

#take guess for the letter and see if in word
def guessletter(word):
    guess = input('Please guess a letter: ')
    guess = guess.upper()
    print('\n\n\n\n\n\n\n')
    if guess == 'QUIT':
        quit()
    indexes = []
    if guess in word:
        for x in range(len(word)):
            if word[x] == guess:
                indexes.append(x)
        return indexes
    return []
    
#runs the game
def game():
    word, rword = start()
    head, rarm, torso, larm, rleg, lleg = ' ', ' ', ' ', ' ', ' ', ' '
    ded = 0
    while True:
        hangman = '  _______.\n  |      |\n  {}      |\n {}{}{}     |\n {} {}     |\n         |\n        /-\\'.format(head, rarm, torso, larm, rleg, lleg)
        print(hangman + '\n\n' + rword + '\n')
        if ded == 6:
            print('You lost!\nThe word was: ' + word)
            quit()
        elif ' '.join(word) == rword:
            print('You win!')
            quit()
        indexes = guessletter(word)
        if indexes == []:
            ded += 1
        for index in indexes:
            rword = rword.split(' ')
            rword[index] = word[index]
            rword = ' '.join(rword)
        if ded == 1:
            head = 'O'
        elif ded == 2:
            torso = '|'
        elif ded == 3:
            rarm = '/'
        elif ded == 4:
            larm = '\\'
        elif ded == 5:
            rleg = '/'
        elif ded == 6:
            lleg = '\\'

game()