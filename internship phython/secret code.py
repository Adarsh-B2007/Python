secret_number= 10
for i in range(1, 5):
    num = int(input("enter the secret number:"))
    if num == secret_number:
       print("secret number is correct")
       break
    elif num<secret_number:
        print("greater than secret number ")
    elif num>secret_number:
        print("less than secret number ")
    else:
        print("secret number is wrong") 
if  num !=secret_number:
    print("game over")
       
       



  