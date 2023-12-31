firstno=input("Enter your first number : ")
operator=input("Enter operator (+,-,*,/,%) : ")
secondno=input("Enter your second number : ")
firstno=int(firstno)
secondno=int(secondno)
if(operator== '+' ) :
    result= ( firstno+ secondno)
    print("Addtion is : " +str(result))
elif(operator== '-' ) :
    result= ( firstno- secondno)
    print("Substraction is : " +str(result))
elif(operator== '*' ) :
    result= (firstno* secondno)
    print("Multiplication is : " +str(result))
elif(operator== '/' ) :
    result= (firstno/ secondno)
    print("Division is : " +str(result))
elif(operator== '%' ) :
    result= (firstno% secondno)
    print("MOduloDivison is : " +str(result))
else:
    print ("Invalid Operator")