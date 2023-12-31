def my_fibonaci(n):
    a=1
    b=1
    output=[]
    for i in range(n):
        #yield a
        output.append(a)
        a,b=b,a+b
    return output
for x in my_fibonaci(7):
    print(x)