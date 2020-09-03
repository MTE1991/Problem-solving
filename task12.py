def remove_odd(any_list):
    return [i for i in any_list if i % 2 == 0]

print(remove_odd([21, 33, 44, 66, 11, 1, 88, 45, 10, 9]))

#output: [21, 33, 44, 66, 11, 1, 88, 45, 10, 9]
