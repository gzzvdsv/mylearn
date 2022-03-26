# # py程序在加载的时候，会给解释器内部的需要的一些内置变量进行加载，加载的位置加
# # 内置名称空间
# # 接下来就开始执行你自己的py文件，你自己创建的
# print('Hello world')
#
#
# a=10
# def func():
#     global a
#     a=20
#     print('fuc里面的a：',a)
# func()
# print('全局的a:',a)
#
#
#
#
# a=0
# def func1():
#     global a
#     print('func1执行')
#     def  func2():
#         print('func2执行')
#     print('func1执行结束',a,'次')
#     func2()
#     if a<100:
#         a+=1
#         func1()
# func1()
#
# # 三个名称空间
# # 1:内置名称空间  python 自己的东西
# # 2：全局名称空间  全局变量
# # 3：局部名称空间   在函数被调用的时候，函数执行完成
# # 注意, 在python中. 你可以认为变量的使用是遵循就近原则的.
# # 在函数外面的变量被称为全局变量. 它的作用域是整个py文件.
# # 在函数内部的变量被称为局部变量.作用范围仅限于函数内部.
# # 我们可以通过globals()和locals()查看全局和局部作用域中的内容
#
# b=10
# def func23():
#     global b
#     print(b)
# func23()
# def func233():
#     # global b
#     print(b)
#     print(locals())
# func23()
#
#
# print(globals())
# print(locals())
# print('=======================')

a = 10


def func1():
    print("a:", a)
    c = 10
    print(locals())  # {'c': 10}  当前作用域中的变量是这些
    def func2():
        d=10
        print(d)
        print(locals())

    print(locals())
    func2()


func1()
print(
    locals())  # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x01599B38>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'G:\\代码相关\\python\\面试+学习笔记\\python课程录制\\python_1_3\\08_变量的作用域和名称空间.py', '__cached__': None, 'a': 10, 'func1': <function func1 at 0x01948808>}
# 全局作用域中的变量是这些
print(globals())
# 函数里面的变量  在使用的时候 会寻找自己最近的 函数里面  没有再找全局 没有再找内置变量
# # 作用域, 一个变量能够发挥作用的范围. 能在哪儿调用
# # 全局作用域, 整个py文件中都可以随意的使用 , 包含全局名称空间+内置名称空间
# # 局部作用域, 只能在局部名称空间中使用的
# # 变量的搜索路径: 先找自己, 然后找外层, 最后找内置