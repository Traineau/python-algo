
def moving_average(list_value, windows_size):
    average_values = []
    while(len(list_value) > windows_size):
        sum = 0
        index = 0
        while(index < windows_size):
            sum += list_value[index]
            index += 1
        average_values.append(sum / windows_size)
        list_value.pop(0)

    return average_values

def moving_average2(list_value, windows_size):
    average_values = []
    # Initialisation
    sum = 0
    init_index = 0
    while(init_index < windows_size):
        sum += list_value[init_index]
        init_index += 1
    average_values.append(sum / windows_size)

    # Moving sum
    index = 0
    while(index + windows_size < len(list_value)):
        # We just remove the element before and append the element after every iteration
        # So we don't have to sum all the numbers in our windows size every time
        sum -= list_value[index]
        sum += list_value[index + windows_size]
        average_values.append(sum / windows_size)
        index += 1

    return average_values

to_analyse = [n for n in range(20)]
to_analyse = [2, 4, 1, 8, 9, 14, 2, 46, 4, 36, 82, 12, 27, 23, 84, 63, 25, 60, 9]
print(moving_average2(to_analyse, 2))
