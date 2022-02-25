#TIPE DATA LIST
list1 = [1,2,3,4,5,6,7,8,9]
print(list1)
print(list1[5])
print(list1[:3])
print(len(list1))
print(list1[10-3:])
print(list1[2:9])
print(list1[-10])
print(list1[0])
list1.append(10)
print(list1)
list1.insert(1,11)
print(list1)

list2 = ['hello']
list1.extend(list2)
print(list1)

list1.extend('hai')
print(list1)

del list1[1]
print(list1)

list1.remove(5)
print(list1)

list1.pop()
print(list1)

a = [50,20,30,40]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(min(a))
print(max(a))

#TIPE DATA DICTONARY
d = {1:100,2:200,3:300,4:400,5:500}
print(d)
print(d[2])
print(d.get(4))
print(d.keys())
print(d.values())
del d[3]
print(d)
d.clear()
len(d)