class Calculator():
    def add(self,a,b):
        c=a+b
        print("adition of two numbers",c)
      
    def remainder(self,a,b):
        c=a%b
        print("remainder of first number",c)

    def multiplication(self,a,b):
        c=a*b
        print("multiplication of two numbers",c)
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
obj=Calculator()
obj.add(a, b)
obj.multiplication(a,b)
obj.remainder(a,b)