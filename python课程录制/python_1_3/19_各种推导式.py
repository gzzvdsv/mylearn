lis = [i for i in range(1, 11)]
print(lis)
# 列表推导式
lis = [i for i in range(1, 11)]
print(lis)
lis = [i for i in range(1, 11)]
print(lis)

lis = [i for i in range(1, 11) if i % 2 == 0]
print(lis)

lis = [i ** 2 for i in range(1, 11) if i % 2 == 1]
print(lis)

lis = ['python x %s' % i for i in range(1, 11)]
print(lis)
# 字典推导式
zp = ['one', 'two', 'three']
lis = ['你好', '你不好', '你很好']
dic = {zp[i]: lis[i] for i in range(len(lis))}
print(dic)
# 
set_={item for item in lis}
print(set_)