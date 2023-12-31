def my_even_list(number_list):
    for number in number_list:
        if number % 2 == 0 :
            return True
        else :
            pass
    return False
print(my_even_list([1,5,7]))