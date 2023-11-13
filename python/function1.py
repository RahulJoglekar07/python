# use of open function to read the file
f=open('first.py','rt')  #by defaul read mode 'r', 'rb'(read binary), 'rt'(read text)

#data=f.read()          # read full

data=f.readline()       # read first line
print(data)

data=f.readline()       # read second line
print(data)

f.close()

