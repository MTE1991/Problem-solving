# task 11
def make_square(numbers):
    d = {}
    for num in range(numbers[0], numbers[1] + 1):
        d[num] = num ** 2
    return d

print(make_square((5,9)))
