a={                                   # Hindi Dictionary
    'panka':'fan',
    'sabsi':'vegitable',
    'ladaka':'boy',
    'ladki':'girl',
    'pustak':'book'
    
}
print('the options are :',a.keys())
b=input('enter the word :\n')
#print('the meaning is :\n',a[b])      # shows error
print(b,'the meaning is :\n',a.get(b))   # not show error









