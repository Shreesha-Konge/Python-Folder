work_hours=[ ('Sai',30000),('Shree',5000),('Konge',800) ]
def employee_list(work_hours):
    current_prices=0
    employee_of_month=''
    for employee,hours in work_hours:
        if hours > current_prices:
            current_prices = hours
            employee_of_month=employee
        else:
            pass
    return (employee_of_month,current_prices)
#print(employee_list(work_hours))
name,workhours=employee_list(work_hours)
print(name)
print(workhours)