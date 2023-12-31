#AVG VALUE OF ALL ELEMENTS IN LIST OF DICTIONARIES
def cal_avg(lst):
    total_sum=0
    count=0
    for d in lst:
        if key_to_avg in d:
            total_sum+=d[key_to_avg]
            count+=1
    if count>0:
        average=total_sum/count
    else:
        average=0
    
    return average
lst=[
    {'val':10},
    {'val':20},
    {'val':30},
    {'val':40}
]
key_to_avg='val'
print(cal_avg(lst))