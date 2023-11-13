def max(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    if (b>c):
        return b
    else:
        return c
m=max(4,6,8)
print(str(m))