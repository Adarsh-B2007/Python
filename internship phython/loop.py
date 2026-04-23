correct_password = "spider man"
for i in range(1, 4):
    num= input("enter your password :")
    if num == correct_password:
        print("successfully login")
        break
    else:
        print("incorrect password")
if  num!= correct_password:
       print("access denied //")
    
