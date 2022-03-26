dic = {'jay': '周杰伦', 'jj': '林俊杰', 'zgr': '张国荣'}

# 1 直接循环 拿到的是key
# for i in dic:
#     print(i,dic[i])

for k,v in dic.items():
    print(k,v)
#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
print(dir(dict))

print(dic.keys())

for  z in dic.keys():
    print(z)
for  z in dic.values():
    print(z)

# 解构
a=(10,1)
print(a)

for item in dic.items():
    print(type(item),'==========',item)