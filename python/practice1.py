a={
    'Rahul':'name',
    'sirsi':'place',
    1:2
}
#print(list(a.keys()))
#print(list(a.values()))
#print(list(a.items()))

b={
    'mango':'fruit',
    'rose': 'flower' 
}

a.update(b)
print(a)

print(a.get('tometo'))

