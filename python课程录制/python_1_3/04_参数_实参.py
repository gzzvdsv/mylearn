# 函数定义时候 可以定义参数默认值  不影响参数 b,c=None  两个是没有去别的  区别是
# a ,b是必须要传入的值 而  c,d是可传可不传  所以函数定义的时候 最关键的几个参数可以这样写
# 在一开始  写上  后面的参数都是不太重要的参数了
def cans(a, b, c=None, d=None):
    print(a, b, c, d)


cans('a', 'b', 'c', 'd')
cans('a', 'b')
# 函数定义时候   是否有默认值 与实际传参时候  无联系
# 不过实际传参过程中  有了关键字参数  后面也是都要使用关键字参数传参方法
def cans(a, b, c=None, d=None):
    print(a, b, c, d)
cans(a='a', b='b')