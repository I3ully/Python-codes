import random
def func(rndm,choice):
    if rndm == 'rock' and choice == 'scissors' or rndm == 'scissors' and choice == 'paper' or rndm == 'purceli' and choice == 'rock':
        print('computer won')
    elif rndm == choice:
        print('draw')
    else:print('user won')
    

signs = ['rock', 'paper', 'scissors']
random_choice = random.choice(signs)

user = input('Enter rock, paper or scissors: ')
func(random_choice, signs)
print(f'Pc chose:{random_choice}')


