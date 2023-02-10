import random
def guess(g, name, count):
    while count < 20:
        count += 1
        x = int(input('Take a guess'))
        if x != g:
            if x < g:
                print('Your guess is too low')
            elif x > g:
                print('Your guess is too high')
        else:
            print('Good job, '+ name +'! You guessed my number in '+ str(count) +'guesses')
            break

name = input('Hello! What is your name?')
print('Well, '+ name + ', I am thinking of a number between 1 and 20.')
g = random.randrange(1, 20)

guess(g, name, 0)
