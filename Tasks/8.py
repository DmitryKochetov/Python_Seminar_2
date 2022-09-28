# 5 Реализовать алгоритм перемешивания списка.

import random

new_array = [1, 3, 6, 9, 8, 5]
temp_for_ndex = 0
temp_for_element = 0

print(new_array)

for i in range(len(new_array)):
    temp_for_index = random.randint(0, len(new_array)-1)
    temp_for_element = new_array[i]
    new_array[i] = new_array[temp_for_index]
    new_array[temp_for_index] = temp_for_element

print(new_array)