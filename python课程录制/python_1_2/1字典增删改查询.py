# key是可哈希的  即是不可变得数据类型    数字  字符串   元组  bool  value 没有任何的要求
# 不能作为key的数据类型有   set  list  dict
# 储存过程  key进行哈希运算  算出要存放的地址 在存放里面的value
# print(dir(set))
# # 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
# # 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
# # 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
# lis = [1, 2, 3, 4, 5, 1, 2, 4, 5]
# print(set(lis))  # {1, 2, 3, 4, 5}

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
dic = {'1': '123', '2': '246', '3': '369'}
# 新增  直接等于 有就直接会修改 没有就会增加
dic['new_1'] = 'new_1'
dic['new_1'] = 'new_2'
print(dic)
dic.setdefault('new_2', 'new_3')  # Python 字典 setdefault() 函数和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
print(dic, "dic.setdefault('new_2', 'new_3')")
print(dic.setdefault('jay'))
print(dic, "print(dic.setdefault('jay'))") # 'jay': None  只写一个的话就会增加这一个东西
# # dic.update()
# dic.pop('new_1')
# dic.pop('new_2')
# print(dic)
# print(dir(list))  # append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# lis = [1, 2, 3, 4]
# print(lis)
# del lis
# # print('liss',lis)
#
#
# # 查询  get (不存在报错)或者 dic[key]  （不存在返回none） ,get也可以指定没有返回值 时候的 返回值   相当于改变 none 的值
# dic = {'jay': '周杰伦', 'jj': '林俊杰', 'zgr': '张国荣'}
# print(dic.get('jay', '弹出'))
# # print(dic['ja'])
# print('============================')
# # 特殊   查询会
# dic = {'jay': '周杰伦', 'jj': '林俊杰', 'zgr': '张国荣'}
# # Python 字典 setdefault() 函数和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
# print(dic.setdefault('jay', 'jj'))
# print(dic)
# # lst=
#
#
# # 练习 [11,12,23,13,14,23,58,59,66,77,88]  以50为分解
# lis = [11, 12, 23, 13, 14, 23, 58, 59, 66, 77, 88]
# # xiao = [i for i in lis if i < 50]
# # da = [i for i in lis if i > 50]
# # dic = {'xiao50': '', 'da50': ''}
# # dic = {'xiao50': xiao, 'da50': da}
# # print(dic)
# # dic = {}
# # for i in lis:
# #     if i < 50:
# #         if dic.get('small')==None:
# #             dic['small']=[i]
# #         else:
# #             dic['small'].append(i)
# #     else:
# #         if dic.get('bigger')==None:
# #             dic['bigger']=[i]
# #         else:
# #             dic['bigger'].append(i)
# # print(dic)
#
#
#
#
# lis = [11, 12, 23, 13, 14, 23, 58, 59, 66, 77, 88]
# res={}
# for i in lis:
#     if i<50:
#         res.setdefault('small',[]).append(i)
#
#     else:
#         res.setdefault('bigger',[]).append(i)
#
# print(res.setdefault('biggers'))
# print(res)
