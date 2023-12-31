#SUM AND AVG USING BUILTIN FUNCTIONS
def sum_avg(my_lst):
    result1=sum((my_lst))
    print( result1)
    result2=result1/len(my_lst)
    print(result2)
my_lst=[10,10,50,30,40]
print(sum_avg(my_lst))