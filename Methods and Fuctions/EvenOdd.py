def numbers_check(number_list):
    even_numbers=[]
    odd_numbers=[]
    for num in number_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else :
            odd_numbers.append(num)
    print('Even numbers are {} '.format(even_numbers))
    print('Odd numbers are {} '.format(odd_numbers))
print(numbers_check([1,2,3,4,5,6,7,8,9,10]))