def multiply(numbers):
    total=1
    for number in numbers:
        total*=number
    return total
numbers=[1,2,-3,-4]
print(multiply(numbers))