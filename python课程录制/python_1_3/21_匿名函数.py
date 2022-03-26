# lambda 表达式
fu = lambda n: n + n
print(fu(10))  # 20
print(fu)  # <function <lambda> at 0x01968808>   匿名函数相较于普通函数没有名字


def fun():
    print('')


print(fun)  # <function fun at 0x0160C2F8> 普通函数有函数名称

funs=lambda a,b:a+b
print(funs(10,20))   #30