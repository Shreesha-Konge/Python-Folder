def cubes(n):
    for i in range(n):
        yield i**3
for x in cubes(5):
    print (x)
    
