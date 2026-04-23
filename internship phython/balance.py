balance = 10000
balance = balance - 2000

with open("bal.txt","w") as  file:
    file.write(str(balance) + "\n" )
print(balance)
balance = balance - 2000       
with open("bal.txt","a") as file:
    file.write(str(balance) +"\n")
print(balance)
balance = balance - 2000
with open("bal.txt","a") as file:
    file.write(str(balance) + "\n")    
print(balance)
balance = balance - 2000
with open("bal.txt","a") as file:
    file.write(str(balance) + "\n")
print(balance)    
    
    
    
    
    
    
    
    
    
    
    