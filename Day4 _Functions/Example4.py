#SQUARES OF ELEMENT
def squares_of_nums(nums_list):
    squared_list=[]
    for n in nums_list:
        squared_item=n**2
        squared_list.append(squared_item)
    return squared_list
nums_list=[1,2,3,4,5,6,7,8,9,100]
print(squares_of_nums(nums_list))