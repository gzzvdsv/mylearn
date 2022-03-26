def wapper1(fn):
    def inner(*args, **kwargs):
        '''被装饰函数之前执行内容'''
        print('wapper1执行之前')
        res = fn(*args, **kwargs)
        '''被装饰函数之后执行内容'''
        print('wapper1执行之后')
        return res

    return inner


def wapper2(fn):
    def inner(*args, **kwargs):
        '''被装饰函数之前执行内容'''
        print('wapper2执行之前')
        res = fn(*args, **kwargs)
        '''被装饰函数之后执行内容'''
        print('wapper2执行之后')
        return res

    return inner


def wapper3(fn):
    def inner(*args, **kwargs):
        '''被装饰函数之前执行内容'''
        print('wapper3执行之前')
        res = fn(*args, **kwargs)
        '''被装饰函数之后执行内容'''
        print('wapper3执行之后')
        return res

    return inner


@wapper3
@wapper2
@wapper1   #按照就近原则进行解读
def ta():
    print('ta函数执行')


# ta()
# wapper3执行之前
# wapper2执行之前
# wapper1执行之前
# ta函数执行
# wapper1执行之后
# wapper2执行之后
# wapper3执行之后

