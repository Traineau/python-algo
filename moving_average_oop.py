import random


class MovingAverage:
    def __init__(self, windows_size):
        self._accumulator = 0
        self._push_index = 0
        self._windows_size = windows_size
        self._fifo_stack = [0] * self._windows_size

    def clear(self):
        self._accumulator = 0
        self._push_index = 0
        self._fifo_stack = [0] * self._windows_size

    def push(self, in_value):
        out_value = self._fifo_stack[self._push_index]
        self._fifo_stack[self._push_index] = in_value

        self._accumulator -= out_value
        self._accumulator += in_value

        self._push_index += 1
        self._push_index %= self._windows_size

        return self._accumulator / self._windows_size

    def get_mean(self):
        return self._accumulator / self._windows_size


max_value = 30
windows_size = 10

my_moving_average = MovingAverage(windows_size)

index = 1
while(index < max_value):
    value = random.randint(1, max_value)
    print(value, my_moving_average._fifo_stack, my_moving_average.push(value))
    index += 1