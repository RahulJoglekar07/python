a=int(input('Enter the num : '))
prime = True
for i in range(2,a):
    if(a%i==0):
        prime=False
        break
if prime:
    print('this num is prime')
else:
    print('this num is not prime')
    



