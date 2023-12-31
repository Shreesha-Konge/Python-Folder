#A = P(1 + R/100) t 
#P-PRINCIPAL,R-RATE OF INTEREST, T-TIME
P=int(input('Enter amount: '))
R=int(input('Interest : '))
T=int(input('Enter Timeperiod : '))
CI=P*(pow((1 +R/100),T))
print(CI)