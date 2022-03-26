a = [1, 2, 3]
# for循环内部大致执行过程
lis = a.__iter__()
print(lis)   #<list_iterator object at 0x017FB9A0>
while 1:
    try:
        print(lis.__next__())
    except  StopIteration as e:
        print('====', e)
        break
        pass


