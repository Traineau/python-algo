# Convertir une valeur decimale en valeur binaire (sous forme de tableau)
def decimal_to_binary(dec_value):
    # On applique un masque un a la valeur decimale
    # L'ordinateur voit la valeur decimale sous forme binaire
    # On va donc avec cela recuperer la valeur du bit de poids faible
    # Exemple : Ma valeur decimale est 7, represente en binaire 0, 1, 1, 1
    # J'applique un masque 1 (donc 0, 0, 0, 1) : ca me donne 1
    # On stocke donc 1 dans notre tableau d'elements binaire
    binary_value = [dec_value & 1]
    # On decale les bits de notre valeur decimale de 2 a droite : On regarde enfait
    # Le bit suivant, et ça divise la valeur par deux
    dec_value >>= 1
    # On fait ça tant que notre nombre ne vaut pas 0
    while dec_value != 0:
        binary_value.append(dec_value & 1)
        dec_value >>= 1
    return binary_value

test1 = 567
print('Convert 567 to Binary : ', decimal_to_binary(test1))


def binary_to_decimal(binary_value):
    decimal_value, bit_weight = 0, 1
    while binary_value:
        decimal_value += binary_value.pop(0) * bit_weight
        bit_weight <<= 1
    return decimal_value


def binary_to_str(binary_value, number_of_displayed_bit):
    bit_index = number_of_displayed_bit - 1
    str_value = ''

    while bit_index >= len(binary_value):
        str_value += '0'
        if (bit_index % 4 == 0):
            str_value += ' '
        bit_index -= 1

    while bit_index >= 0:
        str_value += str(binary_value[bit_index])
        if(bit_index %4 == 0):
            str_value += ' '
        bit_index -= 1

    return str_value

print(binary_to_decimal(decimal_to_binary(567)))

print(binary_to_str(decimal_to_binary(14762842), 32))


# ----------------------- ADDITIONNEUR BINAIRE ---------------------------

def binary_word_adder(binary_value_a, binary_value_b):
    len_a = len(binary_value_a)
    len_b = len(binary_value_b)
    max_binary_value_len = max(len_a, len_b)

    bit_index = 0
    binary_final = []
    carry_out = 0
    while bit_index < max_binary_value_len :

        bit_a = 0
        if(bit_index < len_a):
            bit_a = binary_value_a[bit_index]

        bit_b = 0
        if (bit_index < len_b):
            bit_b = binary_value_b[bit_index]

        bit_s, carry_out = one_bit_adder(bit_a, bit_b, carry_out)

        binary_final.append(bit_s)
        bit_index += 1

    if(carry_out == 1):
        binary_final.append(1)

    return binary_final


def one_bit_adder(bit_a, bit_b, carry_in):
    # Boolean complete adder
    # -> bit_a : Bit status of first operand
    # -> bit_b : Bit status of second operand
    # -> carry_in : input carry
    # <- bit_s : bit status of add
    # <- carry_out : output carry
    tmp = bit_a ^bit_b
    bit_s = tmp ^carry_in
    carry_out = (tmp & carry_in) | (bit_a & bit_b)

    return bit_s, carry_out

print(binary_word_adder([1, 1, 0],[1, 1]))


# ----------------------- Reverse numerical value ----------------------------


def to_bit_reverse(natural_value, n_bit):
    reversed_value = natural_value & 1
    natural_value >>= 1
    bit_index = 1
    while bit_index < n_bit:
        reversed_value <<= 1
        reversed_value |= natural_value & 1
        natural_value >>= 1

        bit_index += 1

    return reversed_value



print(to_bit_reverse(8, 4))