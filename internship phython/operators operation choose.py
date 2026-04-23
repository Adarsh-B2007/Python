a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
operation = input("Enter the operation you want to perform (+, -, *, /):")  
if operation == "+":
    print("The result is ", a+b)      
elif operation == "-":
    result=a-b
    print("The difference of", a, "and", b, "is", result)
elif operation == "*":
    result = a * b
    print("The multiplication of", a, "and", b, "is", result)           
elif operation == "/":
    if b != 0:
        result = a / b
        print("The division of", a, "by", b, "is", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("invalid operation"
          )

        
