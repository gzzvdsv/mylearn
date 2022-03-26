# 形参 代码补全  完成函数的编写 表示函数需要  这个参数
# 实参  实际函数执行是传递值  表示实际传进去了  这个参数 具体值
# 传参 给函数传递信息  时候 实际数据传递给函数的过程叫传参
# 位置参数  按照顺序  给参数赋值

# def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
# 以这个函数为例子   第一个是位置参数  后面的是关键字参数

def chuacas(a, b, c):
    print('a:', a, 'b:,', b, 'c:', c)


chuacas('c', 'b', 'a')


# 关键字参数   如果函数有多个参数  快速区分

def chuacas(a='', b='', c=''):
    print('a:', a, 'b:,', b, 'c:', c)


# 函数执行过程中 以第一个关键字传入为开始  使用关键字传参
chuacas(a='c', b='b', c='a')


# 混合传参   混合传参的时候 需要关键字传参在位置参数后面
def chuacas(a, b='', c=''):
    print('a:', a, 'b:,', b, 'c:', c)


chuacas(a='c', b='b', c='a')


# 位置参数可以 使用关键字传参方法传入参数
def yue(ap=''):
    print('ap', ap)


yue(ap='关键字')
yue('位置输入')
# with open()
# def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
# 以这个函数为例子   第一个是位置参数  后面的是关键字参数  可以看到    关键字后面使用 位置传参报错了  但是前两个使用位置传参是可以使用的
with open('1.txt', 'r', encoding='utf-8') as f:
    print(f.read())
