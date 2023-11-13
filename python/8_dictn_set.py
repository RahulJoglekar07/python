MyDic = {
    'Rahul':'the name',
    'sirsi': 'one place',
    'mark':[1,2,3],
    1:2
}

#print(MyDic['mark'])

#Methods of Dictionary
print(list(MyDic.keys()))
print(MyDic.values())
print(MyDic.items())  #to print all values in dic

a={
    'Mango':'fruit',
    'tometo':'vegitable',
    'Rahul':'cricketer'   
}

MyDic.update(a)
print(MyDic)
print(MyDic.get('Rahul1'))
