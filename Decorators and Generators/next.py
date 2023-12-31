def simple_gen(n):
    for x in range(n):
        yield x
#print(simple_gen())
#for num in range(3):
 #   print(num)
g=simple_gen(3)
print(next(g))
print(next(g))
print(next(g))