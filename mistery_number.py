import random

max_random = 1000
mysterious_nb = random.randint(1, max_random)
tries_count = 0
is_found = False

while not is_found :
    user_guess = int(input('N ?='))
    tries_count += 1
    if(user_guess > mysterious_nb):
        print('Trop grand')
    elif(user_guess < mysterious_nb):
        print('Trop petit')
    else:
        is_found = True

print('Trouvé en', tries_count, 'essais')