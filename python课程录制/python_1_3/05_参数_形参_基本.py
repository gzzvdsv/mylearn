def funs(var='var',lis=[]):
    lis.append(var)
    print(lis,id(lis),var,id(var))
# 列表有一个默认值  会一直导致  没有传入的话会导致  列表一直使用一个
# 解决方法：可以不设置默认值    列表参数放在一开始就好了
funs(100)
funs(200)
funs()
funs()
funs(lis=[])
