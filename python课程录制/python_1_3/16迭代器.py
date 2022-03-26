a=[1,2,3]
# print(dir(a))     
b=a.__iter__()
print(b.__next__())
print(b.__next__())
print(b.__next__())

# print(b.__next__())
print('__iter__' in dir(a))