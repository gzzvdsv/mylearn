a=[1,2,3]
print(dir(a))
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
 '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
  '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
重点 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
#  增加  append  extend
# 删除  pop (返回删除值) remove  clear  del 切片删除
# del	del L[i]	①根据索引删除；②删除索引范围内的元素；③删除整个列表。del操作没有返回值
# pop	list.pop（i）	根据索引删除，返回索引位置的元素
# remove	list.remove（value）	删除第一个符合条件的元素，注意不是根据索引删除


# 修改  list[i]='value'
# a.pop()
# print(a)
# a.remove(2)
# print(a)

a[1]='xcvzv'
print(a)
