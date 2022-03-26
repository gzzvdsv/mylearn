


def oad(n):
    return n%2==1
print(oad(10))
zp=filter(oad,[1,2,3,4,5,6,9,7,8,9,])
print(zp)
def is_odd(n):
    return n % 2 == 1
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
# 深拷贝  浅拷贝
# 直接等于  原先的改了 后面的也会直接改
# copy.copy  原先的改了后面的不会变  仅限一层 不包括子类
# copy.deepcopy  子类也会直接复制过去
#  直接赋值  直接引用对象  别名
# 浅拷贝 拷贝父类对象不会拷贝对象内部的子类对象
# 深拷贝 deepcopy  完全拷贝了父对象及其子类对象

import copy
a=[1,2,3,4,["a","b",["av"]]]
b=a

c=copy.copy(a)
d=copy.deepcopy(a)
a.append(10)
a[4].append("c")
a[4][2].append("c")
print('直接赋值',b)
print('copy.copy 子类修改会改变值',c)
print("copy.deepcopy",d)

# 列表操作   空值  去重  排序
list_=["a","v","b","c","",""]
new_list=[]
for i in list_:
    if i!="":
       new_list.append(i)
print(list_)
print(new_list)

# 去重1  set  2 keys()  3循环遍历法   4 按照索引再次排序
lis=[0,1,2,3,0,1,3,4]
print(list(set(lis)))
# 2
orgList = [1,0,3,7,7,5]
#list()方法是把字符串str或元组转成数组
formatList = list({}.fromkeys(orgList).keys())
print (formatList)

# 结束循环的几个关键符   exit 直接推出py文件  余下的全都不执行  break pass  continue
bool_flag_1=False
while True:
    while True:
        bool_flag_2=False
        for i in range(3):
            if i==2:
                bool_flag_2=True
                break
        #         这个break是if判断的东西  跳出   for 循环
        print('跳出最里面的循环')
        if bool_flag_2==True:
            bool_flag_1=True
            break
    #         这个break是if  判断里面东西 跳出第二个 while true
    print("跳出稍微外面的一个循环")
    if bool_flag_1==True:
        break
        #         这个break是if  判断里面东西 跳出第一个 while true
print("跳出第三个循环")

flf=0
while True:
    for i in range(10):
        print('i---',i)
        if i==5:
            flf = 1

            break
    if flf==1:
        break
    #         exit()
print('i---')

# 装饰器


def hi(name="yasoob"):
    return "hi " + name

print(hi())
# print(hi())
# output: 'hi yasoob'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个

print(greet())
# output: 'hi yasoob'
new_=hi
print("new_",new_())

del hi
# print(hi())
print("new_",new_())
# 如果我们删掉旧的hi函数，看看会发生什么！
# del hi
# print(hi())
# outputs: NameError

# print(greet())
# outputs: 'hi yasoob'




class use_i():
    def hanshu_(self):
        print("hanshu")

    def use_it(self):
        print("use_it")


    print("class use_is")
use_i()
us=use_i()
us.use_it()


# 函数   基础数据类型  中 不可变的有 数字 字符串   可变的有  列表 元组 字典
def  changss(nas):
    nas.append(10)
    print(nas)
zp=[1,2,3]
changss(zp)
print(zp)

# 必须传一个参数不然会报错
changss([1,23])
# 可以进行关键字传参
changss(nas=[1,2,3])

# 更清晰的展示关键字传参
def  to_(id,namea):
    print("id：",id,"namea:",namea)
to_(id="0-id",namea="0-namea")

# 默认参数  此时可以不穿参数值
def morencanshu(ids="zxcvzxv"):
     print(ids)
morencanshu("newsss")

# 不定长参数
def buxingchang(func,*args,funcxx):
     print(func)
     print(*args)
     print(funcxx)
buxingchang("func","args1","args2","args3",funcxx="funcxx")
# 双星号的是用来收集其他的关键字传参的   表现形式为  字典
def buxingchangshuangxinghao(func,**kwargs):
    print(func)
    print(kwargs)
buxingchangshuangxinghao(func="--func",funzzcv='zxcvzxv')

# lambda  函数
# 函数是一个表达式 函数体比def  简单很多
# 主体是一个表达式而不是一个函数块  尽可以封装有限的逻辑内容
# 函数有自己的  命名空间 而且不能访问 之外自有参数列表和全局变量里面的内容
sums=lambda a,b:a+b
print(sums(10,20))


# 列表表达式







# 五种基础数据类型  数字  字符串  列表  元组  字典
# 其中的可变和不可变指的是
# 不可变对象 该对象指向的内存不可改变  当改变内容的时候会直接 开辟出一个新的内存空间来存储
# 可变对象
a=10
print(a)

b=10
print(id(a))
print(id(b))
list_=[1,2,3,4,10]
print(id(list_))
print(id(list_[4]))