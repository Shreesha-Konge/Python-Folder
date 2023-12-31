#TO FIND UNION,INTERSECTION,DIFFERENCE
def two_sets(set1,set2):
    union_result=set1.union(set2)
    intersection_result=set1.intersection(set2)
    difference_result=set1.difference(set2)
    print(f'Union is :{union_result}')
    print(f'Intersection is : {intersection_result}')
    print(f'Difference is : {difference_result}')
set1={1,2,3,4,5,6,7,8}
set2={1,2,3,9,10,11,12}
result=two_sets(set1,set2)
print(result)    