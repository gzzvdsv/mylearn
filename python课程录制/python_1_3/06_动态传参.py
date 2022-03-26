# *args  **args
# 实参：
#     1.位置参数
#     2.关键字参数
#     3.混合参数，先位置，后关键字
# 形参：
#     1.位置参数
#     2.默认值参数
#     3.动态传参
# *args 是元组   kwargs 是字典
# 形参定义时候  定义的顺序
def func(a, b, c, *args, d=None, e=None, **kwargs):
    print(a, b, c, args, d, e, kwargs)


# func(1,2,3,4,5,6,7,d=8,e=19,f=23,g=123123)

def func(*args, **kwargs):
    print(args)
    print(kwargs)


# func(1, 2, 3, 4, 5, 6, 7, d=8, e=19, f=23, g=123123)
# def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
# *args前面是位置传参  后面是默认值
print('a', 'b', 'c', 'd', 'e',sep='==',end='\n',file='1.txt')
print('a', 'b', 'c', 'd', 'e',sep='==',end='\t')

