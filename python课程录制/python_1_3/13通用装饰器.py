# 装饰器的雏形
# def wapper(fn):
#     def inner(*args,**kwargs):
#         print('开挂')
#         fn()
#         print('关闭外挂')
#     return inner
#
# @wapper
# def dnf():
#     print('dnf启动')
#
# dnf()


# 带参数
# def wapper(fn):
#     def inner(*args,**kwargs):
#         print('开挂')
#         fn(*args,**kwargs)
#         print('关闭外挂')
#     return inner
#
# @wapper
# def dnf(username,password):
#     print('dnf启动',username,password)
#
# @wapper
# def wzry(vx):
#     print(f'{vx}登录启动王者荣耀')
#
# # dnf("admin","123456")
# wzry('gzz')


# 带有返回值
def wapper(fn):
    def inner(*args, **kwargs):
        print('开挂')
        res = fn(*args, **kwargs)
        return res
        print('关闭外挂')

    return inner


@wapper
def dnf(user, pwd):
    print(f'dnf启动账号{user},密码{pwd}')
    return '剑'


# zp = dnf('gzz','123')  # 实际执行的是 inner函数
# print('我得到了一把', zp)


# 函数嵌套
def hsn():
    print('没有返回值')
    return 'hsn的返回值'


def hsnn():
    zp = hsn()
    return zp
    pass


# zp=hsn()
# print('hsn的返回值是',zp)
# zp=hsnn()
# print('hsnn的返回值是',zp)


# 装饰器通用写法
def wapper(fn):
    def inner(*args, **kwargs):
        '''被装饰函数之前执行内容'''
        res = fn(*args, **kwargs)
        '''被装饰函数之后执行内容'''
        return res
    return inner


# 登录判断
flag = False


def wapper(fn):
    def inner(*args, **kwargs):
        '''被装饰函数之前执行内容'''
        while 1:
            if flag:
                res = fn(*args, **kwargs)
                return res
            else:
                login()
        '''被装饰函数之后执行内容'''

    return inner


def login():
    global flag
    user = input('请输入用户名')
    pad = input('请输入密码')
    if user == 'a' and pad == '1':
        flag = True
        print('登录成功 flag=True ')


@wapper
def add():
    print('执行add操作')


@wapper
def upd():
    print('执行upd操作')


# add()
# add()
# add()
# add()
# add()
# upd()
# upd()
# upd()
# upd()
# upd()



# add 装饰器跑5次
flag = False


def wapper(fn):
    def inner(*args, **kwargs):
        '''被装饰函数之前执行内容'''
        while 1:
            if flag:
                res = fn(*args, **kwargs)
                res = fn(*args, **kwargs)
                res = fn(*args, **kwargs)
                res = fn(*args, **kwargs)
                res = fn(*args, **kwargs)
                res = fn(*args, **kwargs)
                return res
            else:
                login()
        '''被装饰函数之后执行内容'''

    return inner


def login():
    global flag
    user = input('请输入用户名')
    pad = input('请输入密码')
    if user == 'a' and pad == '1':
        flag = True
        print('登录成功 flag=True ')


@wapper
def add():
    print('执行add操作')


@wapper
def upd():
    print('执行upd操作')

add()