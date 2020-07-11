import random
# from builtins import None

limit = int(input("Please Enter the Upper Limit for the Game."))
guess = random.randint(0, limit)
print(guess)  #TODO: Remove it afterwards
inp = None
print('''Press 'q' to Quit''')
chk = 0
while inp != guess:
    inpStr=input('Please Enter the Number between 0 and {0}:'.format(limit))
    if inpStr.isnumeric():
        inp = int(inpStr)
        if inp==guess and chk==0:
            print('You Guesed it right the first time!')
        elif inp==guess and chk>=int(limit/2):
            print('You finally guessed it right...')
        elif inp==guess:
            print('You have guessed it right!!!')
        elif inp>guess:
            print('Guess a little lower')
        else:
            print('Guess a little higher')
    else:
        if inpStr == 'q':
            break
        else:
            print('''Press 'q' to Quit''')
    chk += 1
