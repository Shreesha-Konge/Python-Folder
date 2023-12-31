def Calculator(num1,num2,operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid Operator')
num1=int(input('Enter first number : '))
num2=int(input('Enter second number : '))
operator=input('Select one (+,-,*,/)')
result=Calculator(num1,num2,operator)
print("Result is ", result )