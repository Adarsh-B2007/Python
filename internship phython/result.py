import submarks
marks = []
for i in range(1, 6):
    m = int(input("Enter subject marks: "))
    marks.append(m)
    
A = submarks.subject(marks)
B = submarks.average(marks)
C = submarks.result(B)

print("sum is: ", A)
print("Avg of marks: ", B)
print("Result: ", C)
    

