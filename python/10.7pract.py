m=int(input("enter your marks:\n"))
if m>=90:
    g = 'Ex'
elif m>=80:
    g = 'A'
elif m>=70:
    g = 'B'
elif m>=60:
    g = 'C'
elif m>=50:
    g = 'D'
else:
    g = 'fail'
print("you are grade is :", g)