#convert days into years,weeks, days
days=int(input('Enter days : '))
years=days//365
weeks=(days%365)//7
remaining_days=(days %365 )% 7
print(f'{days} days is appoximately {years} years, {weeks}weeks,{remaining_days}days')