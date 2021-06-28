num1 =float(input("Please enter first number:"))
operator=input("Please enter an operator:")
num2 =float(input("Please enter second number:"))

if operator=="+":
    print (num1 + num2)
elif operator == "-":
    print("answer is:" + str(num1 - num2))
elif operator=="*":
    print("answer is :" + str(num1*num2))
elif operator== "/":
    print("answer is :" + str(num1/num2))
else:
    print ("Invalid Operator")

