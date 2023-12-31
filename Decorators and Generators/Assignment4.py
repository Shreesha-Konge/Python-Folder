def my_gen(n):
    for i in range(n):
        yield i*2
    return i
for num in my_gen(3):
    print(num)