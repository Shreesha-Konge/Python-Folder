#CLASS REPRESENT BASIC ADD,SUB,MUL,DIV
class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
c=Calculator()
result_add=c.add(5,5)
result_sub=c.sub(10,7)
result_mul=c.mul(10,8)
result_div=c.div(8,4)
print(f'Addition is : {result_add}')
print(f'Substraction is : {result_sub}')
print(f'Multiplication is : {result_mul}')
print(f'Division is : {result_div}')