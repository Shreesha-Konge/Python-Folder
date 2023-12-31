def squares_nums(n):
    for i in range(n):
        yield i**2
    return i
for num in squares_nums(10):
    print(num)
