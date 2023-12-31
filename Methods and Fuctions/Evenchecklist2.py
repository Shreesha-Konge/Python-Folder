def my_even_checklist(num_list):
    even_numbers=[]
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else :
            pass
    return even_numbers
print(my_even_checklist([1,2,3,4,5,6]))