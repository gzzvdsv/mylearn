"""
*和**:
    在形参部分：聚合 *把位置参数聚合成元组
               **把关键字参数聚合成字典
    再实参部分:打散,把可迭代对象转换成位置参数，把字典转化成关键字参数
    解包
"""


def ars(*args):
    print(args)


lis = ['小王', '小红', '小兰', '小贝', '']
ars(lis[0], lis[1], lis[2], lis[3], lis[4])
ars(*lis)


# a=*lis
# print(a)
# print(type(*lis))
def dic_ars(**kwargs):
    print(kwargs)


dic = {'小王': '15', '小红': '15', '小兰': 16}
dic_ars(**dic)
