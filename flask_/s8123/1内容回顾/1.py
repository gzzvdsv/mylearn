def wapper(func):
    def inner(*args, **kwargs):
        print('inner')
        print(func.__name__)
        return func(*args, **kwargs)

    print('wapper')
    return inner


'''
1 执行 wapper 函数，并将被装饰的函数当作参数 wapper(index)
2 将第一步的返回值，重新赋值给 新index = wapper(老 index)
'''


@wapper
def index(a):
    return a


zp = index(10)
print(zp)
