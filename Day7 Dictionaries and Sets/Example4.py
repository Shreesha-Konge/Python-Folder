#TWO SETS HAVE COMMON ELEMENTS
def two_sets(set1,set2):
    common_elements=set1.intersection(set2)
    return common_elements
set1={1,2,3,4,5,6}
set2={2,3,4,8,9,10}
print(two_sets(set1,set2))