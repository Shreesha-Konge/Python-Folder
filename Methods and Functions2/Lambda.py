square=lambda num:num**2
print(square(2))
lambda num:num**2
mylist=[1,2,3,4,5,6]
print(list(map(lambda num:num**2,mylist)))
lambda num:num%2==0
print(list(filter(lambda num:num%2==0,mylist)))