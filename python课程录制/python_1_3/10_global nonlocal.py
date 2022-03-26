# a = 10
#
#
# def func1():
#     global a  # 把全局内容引用到局部
#     a = a + 1
#     print(a)
#
#
# func1()


def func1():
    a = 10

    def func2():
        nonlocal a   #nonlocal 调用的变量必须是局部变量  函数体里面新定义的变量 
        a += 1
        print(a)

    func2()


func1()
