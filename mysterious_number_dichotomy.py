# Nombre mystère par dichotomie
import random

max_limit = 100
tries_count = 0
is_found = False
guess_inf = 1
guess_sup = max_limit

mysterious_number = int(input('Choisissez un nombre entre 1 et 100:'))
while not is_found:
    guess = (guess_inf + guess_sup) // 2
    tries_count += 1
    if guess < mysterious_number:
        guess_inf = guess
        print(guess, 'Trop petit')
    elif guess > mysterious_number:
        guess_sup = guess
        print(guess, 'Trop grand')
    else:
        print(guess)
        is_found = True

print("Trouvé en ", tries_count, " essais.")