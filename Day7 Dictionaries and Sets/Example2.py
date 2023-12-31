#MOST FREQUENT ELEMENT IN LIST
def most_frequent_element(lst):
    d1={}
    for item in lst:
        if item in d1:
            d1[item]+=1
        else:
            d1[item]=1
    frequent_element=max(d1,key=d1.get)
    return frequent_element
lst=[11,2,3,4,4,4,4,5]
print(most_frequent_element(lst))

