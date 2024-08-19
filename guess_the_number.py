import random
print('Hello there in this code you will guess the random number.')

random_number=input('enter the the end of range that you want to guess between it ')

if random_number.isdigit():
    random_number = int(random_number)
    if random_number <= 0:
        print('please enter a number bigger than 0 next time. ')
        quit()
else:
    print('enter an number next time. ')
    quit()

r=random.randint(0,random_number)
guesses=0

while True:
    guesses=guesses+1
    user_guess=input('enter the number: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('enter a number next time. ')
        continue 
    if user_guess == r :
        print(' great! you guess it correct.')
        break 
    elif user_guess > r :
        print('your guess is above the number try again. ')
    else:
        print('your guess is below the number try agian. ')
print('you got it in ',guesses,'guesses')
