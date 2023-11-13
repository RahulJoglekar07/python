a='''Hello name 
How are u? I think you are Good.
Congrgulations Your ticket for
goa is sucessfully Booked on the Date:date'''

name=input('Enter Your Name :\n')
date=input('Enter the date when you want to go Goa :\n')

a=a.replace('name',name)
a=a.replace('date',date)

print(a)



