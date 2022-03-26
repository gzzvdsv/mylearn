# 装饰器通用写法
def wapper(fn):
    def inner(*args, **kwargs):
        '''被装饰函数之前执行内容'''
        print('''被装饰函数之前执行内容''')
        res = fn(*args, **kwargs)
        print('''被装饰函数之后执行内容''')
        '''被装饰函数之后执行内容'''
        return res

    return inner


@wapper
def app__(x, y):
    print('__app__', x, y)


app__(10, 11)
