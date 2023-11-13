a= [1,2,3,4,5,6,7,8]
print(a)

print(a[4])    #print value from list

a[4]=9         #change value
print(a)

#list can contain any char
b=[1,'rahul',True,2,3,4,5]
print(b[1])

#list slicing
f=['rahul','tom','raju',23]
print(f[-3:])

#list methods
L1=[1,8,7,2,21,15]
L1.sort()
print(L1)

L1.reverse()
print(L1)

L1.append(45)  #add value at end 
print(L1)

L1.insert(3,544) #insert at position
print(L1)

L1.pop(2)  #delete value at end 
print(L1)

L1.remove(21)  #delete value at end 
print(L1)



