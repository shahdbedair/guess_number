print('please think of a number between 0 and 100')
low= 0
high = 100
medium = (low+high)//2
state = True
while state:
    print('is your secret number '+str(medium))
    guess = input("enter 'h' to indicate the guess is too high. enter'l' to indicate the guess is too low. enter 'c' to indicate i guessed correctly")
    if guess =='c':
        print('game over. your secret number was: '+str(medium))
        state = False
    elif guess == 'h':
        high = medium
        medium = (low+high)//2
    elif guess == 'l':
        low = medium
        medium = (low + high)//2
    else:
        print('sorry, i did not understand your input.')
        
