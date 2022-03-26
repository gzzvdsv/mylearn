# 内层函数调用外部变量
a = 10


def func1():
    # 没有这个会报这个错误
    # UnboundLocalError: local variable 'a' referenced before assignment
    # 局部变量在  引用 之前赋值  referenced 引用   assignment  赋值
    global a

    print('a:', a)
    a = a + 10
    print(a)


func1()
