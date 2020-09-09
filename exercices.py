# ------------------- Basic exercices -----------------


def sum_list(list):
    sum = 0
    while list:
        sum += list.pop(0)

    return sum


print(sum_list([3, 5, 4]))


def erathostene_sieve(limit):
    # Erathostene Sieve
    # -> limit : Limit of the list
    # <- prime_numbers : List of the prime numbers
    is_prime = [True] * (limit + 1)

    number_to_test = 2
    while number_to_test * number_to_test <= limit:
        if is_prime[number_to_test]:
            second_index = number_to_test * 2
            while second_index <= limit:
                is_prime[second_index] = False
                second_index += number_to_test
        number_to_test += 1

    prime_numbers = []
    index = 0
    while index <= limit:
        if is_prime[index]:
            prime_numbers.append(index)
        index += 1

    return prime_numbers


print(erathostene_sieve(120))


def reverse_list(list):
    index_inf = 0
    index_sup = len(list) - 1

    while index_inf < index_sup:
        list[index_inf], list[index_sup] = list[index_sup], list[index_inf]
        index_inf += 1
        index_sup -= 1

    return list


print(reverse_list([1, 4, 7, 3, 9, 11]))