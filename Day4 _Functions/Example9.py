def leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return 'LEAP YEAR'
    else:
        return 'NOT A LEAP YEAR'
year=int(input('Enter  a  year: '))
print(leap_year(year))