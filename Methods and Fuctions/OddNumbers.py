def my_odd_checklist(checklist):
    odd_numbers=[]
    for num in checklist:
        if num % 2 ==1:
            odd_numbers.append(num)
    return odd_numbers
print(my_odd_checklist([1,2,3,4,5,6,7,8]))   

        