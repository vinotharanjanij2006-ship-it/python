print("Simple Calcuator")

print("Select Operation")
print("1.Add")
print("2.Subraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("Enter your choice:"))
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

if choice==1:
    print("Result",num1+num2)
if choice==2:
    print("Result",num1-num2)
if choice==3:
    print("Result",num1*num2)
if choice==4:
    print("Result",num1/num2)
else:
    print("Invalid choice")