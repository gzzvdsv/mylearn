# 可以在不改变原有代码基础，给函数添加新的功能
# 可以在原有操作前面或者后面随意添加新的功能
# 语法糖
def wapper(fn):
    def inner(*args,**kwargs):
        print('执行之前的输出')
        fn()
        print('执行之后的输出')
    return inner
    # return fn
@wapper
def add():
    a=10
    print('a',a)
# 在不改变原有函数的基础上改变函数的功能
# add=wapper(add)
add()
print(add.__name__)