class Calculator():
    def add(self,a,b):
        c=a+b
        print(c)
      
    def remainder(self,a,b):
        c=a%b
        print(c)

    def multiplication(self,a,b):
        c=a*b
        print(c)
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
obj=Calculator()
obj.add(a, b)
obj.multiplication(a,b)
obj.remainder(a,b)