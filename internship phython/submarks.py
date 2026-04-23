def subject(marks):
    return sum(marks)
def average(marks):
    return sum(marks) / len(marks)
def result(avg):
    if avg >= 50:
        return("pass")
    else:
        return("fail")
     
