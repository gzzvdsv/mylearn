g=(i for i in range(10))
print(g)  #<generator object <genexpr> at 0x0136DD48>

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# 使用set把剩下的  生成器内容全部取出来
print(set(g))

def func():
    print('111')
    yield 222
g=func()
g1=(i for i in g )
g2=(i for i in g1 )
# 第一个才会有数据  其余的都没有数据
print(list(g1))
print(list(g))
print(list(g2))

