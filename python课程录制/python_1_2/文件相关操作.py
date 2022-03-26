import os
# with open("1.txt",mode='r',encoding='utf-8') as f1,\
#     open ('1_副本.txt',mode='w',encoding='utf-8') as f2:
#     for line in f1:
#         if '的' in line:
#             line=line.replace('的','--的--')
#         f2.write(line)
# os.remove('1.txt')
# os.rename('1_副本.txt','1.txt')
import re

# 读取规则文件    以字典形式存储  二维的字典
with open('2.txt', mode='r', encoding='utf-8') as f:
    a = 0
    lis = []
    for line in f:
        print(type(line))
        line = line.strip()  # 去掉读取出来的左右两边的空白
        if a == 0:
            biaotou = (re.split(r'[ ]+', line))
            print(re.split(r'[ ]+', line))
        else:
            lis.append(re.split(r'[ ]+', line))
            pass
        a += 1
ne_lis=[]

for j in lis:
    dic={}
    for i in range(len(biaotou)):
        dic.update({biaotou[i]:j[i]})
    ne_lis.append(dic)
print(ne_lis)
