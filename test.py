a = 1
def some_def(arg):
    res = arg + 1 # 2
    arg += 2 # 3
    print(arg) # 3
    print(res) # 2
    return res
print(some_def(a)) # 2
print(a) # 1

a = {'a': 1, 'b': 2}
def some_def2(arg):
    x = arg
    x['a'] += 2
    print(x) # {'a': 3, 'b': 2}
    arg['c'] = 3
    print(arg) # {'a': 3, 'b': 2, 'c':3}
    return x
print(some_def2(a)) # {'a': 3, 'b': 2, 'c':3}
print(a) # {'a': 3, 'b': 2, 'c':3}


a = [1,2,3,4]
for index, item in enumerate(a):
    temp = a[index] # temp=2
    a[index] = a[(len(a)-1)-index] # a[0] = 4, a[1]= 3
    a[len(a)-index-1] = temp #a[3]=1, a[2]=2
    if index == (len(a)/2-1) :
        break
print(a)


a = [1,2,3,4,5]
for index, item in enumerate(a):
    temp = a[index] # temp=2
    a[index] = a[(len(a)-1)-index] # a[0] = 4, a[1]= 3
    a[len(a)-index-1] = temp #a[3]=1, a[2]=2
    if index == (len(a)//2) :
        break

print(a)






