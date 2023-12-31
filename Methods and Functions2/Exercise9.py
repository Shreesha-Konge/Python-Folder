def blackjack(a,b,c):
        if sum((a,b,c)) <= 21:
            return sum((a,b,c))
        elif sum((a,b,c))<=31 and 11 in (a,b,c):
            result=sum((a,b,c))-10
            return result
        else:
             return 'BUST'

print(blackjack(11,21,1))