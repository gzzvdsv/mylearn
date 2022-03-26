# python for 循环里面 对应不同的数据结构
# 基础数据类型结构  字符串  列表   元组 直接取出值进行迭代   数字无法进行直接迭代 （dir(int)） 里面没有__iter__ 数字用range
# range(start,stop(,step))
#
# for 循环的原理是 迭代器  __iter__ 取出里面的元素进行遍历迭代    iter 可以节省内存在一些数据量大的情况下可以使用
# iter  判断一个对象是否是可迭代的  可以用 dir(对象，或者数据类型)  其中对象的数据类型可以用  type函数查看
#  dir  看对象可以 执行的函数有哪些   其中 __iter__ 就可以迭代
# 字符串
for i in 'abv':
    print(i)
# 列表
for i in [1, 2, 3]:
    print(i)
# range函数    range(start,stop[,setp])
print(type(range(10)))
#
# print(dir(list))
print(dir(range))
print(dir(range(10)))
# range 函数python3 返回的是一个  可迭代对象  rnage对象而不是列表
# list 函数用于将  元组或者字符串转换为列表
zp = type(type(list))
pass
print(type(type(list)))

# 迭代器   迭代是python 最强大的功能之一，是访问集合元素的一种形式
a = 'abcad'
itera = iter(a)
print('========================')
print(itera)  # <str_iterator object at 0x010ABB80>  字符串迭代器
# 迭代器 是一次性的  只能从前往后走    走完了需要重新生成 无法逆向遍历元素
# 迭代器 进行遍
for i in itera:
    print(i)
itera = iter(a)
print('===================')
print(next(itera))
print(next(itera))
# print(next(itera))
# print(next(itera))
# print(next(itera))
# print(next(itera))
# print(next(itera))
# print(next(itera))
# print(next(itera))

print('===================')
print('===================')
print('===================')
print('===================')

# 下面两个理解是等价的
for i in 'abv':
    print(i)
print(i)
for i in iter('abv'):
    print(i)
print(i)

#
# for i in 5:
#     print(i)
print('__iter__' in dir(tuple))

for i in (1, 2, 3):
    print(i)
print(i)
for i in iter((1, 2, 3)):
    print(i)
print(i)

# range函数 使用方法  一个元素  的时候  0-元素 数字  以全部迭代出来
# 两个的时候   前面的默认是开始  后面的结束  全部迭代
#  三个的时候 开始结束step  数字列表切片
print(list(range(-10, 0, 1)))
# 列表取值   列表的索引  [0,1,2,3,4]  通过索引可以取值  截取 切片 等操作
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[::])




# 一个事情的结束是另一些事情的起点