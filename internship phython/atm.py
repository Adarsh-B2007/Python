amount = 20000
while True: 
    print("1.withrawal")
    print("2.check balance")
    print("3. thank you ")
    
    choice = int(input("enter your choice :"))
    if choice == 1: 
     withdraw = int(input("enter amount:  "))
     if withdraw <= amount:
       amount -= withdraw
       print (" succesfully withdrawed ")
     else:
         print ("insufficient balance ")
    elif choice ==2:
         print("the balance is :",amount)
         break
    elif choice ==3:
        print("thank you")
        break
