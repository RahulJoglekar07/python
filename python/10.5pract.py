text=input("enter the tex :\n")

if('make a lot of money' in text):
    spam=True
elif('buy now' in text):
    spam=True
elif('click this' in text):
    spam=True
elif('subscribe this' in text):
    spam=True
else:
    spam=False
    
if(spam):
    print('this text is spam')
else:
    print('this text is not spam')



# to check wether entered word is less than or greater than 10

a=input('enter the word :')
if(len(a)<10):
    print('entered word is less than 10 :')
else:
    print('entered wor is more than 10 :')














