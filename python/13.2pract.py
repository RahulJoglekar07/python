def max(num1,num2,num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    if (num2>num3):
        return num2
    else:
        return num3
    
m=max(11,12,13)
print('the max value is:',str(m))