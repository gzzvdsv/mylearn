# xp=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

xp=[['chine', 213, 13, 43],
    ['znsfdf', 123, 1244, 24],
    ['ewer', 123, 1244, 54],
    ['iwer', 32, 1244, 234],
    ['ose', 234, 45, 234]]


#输入 内容
# for i in range(5):
#     xp_lis=input().split()
#     for j in range(4):
#         if j>=1:
#             xp_lis[j]=int(xp_lis[j])
#         xp[i][j]=xp_lis[j]
delss=[1,2,3,1,2]
for yy in delss:
    b=[i[yy] for i in xp ]
    max_=max(b)
    index_=([i for i,x in enumerate(b) if x==max_])
    if len(index_)>1:
        toubu=[]
        for i in range(len(index_)):
            toubu.append(xp[index_[i]][0])
        b=[i[0] for i in xp]
        print(xp[b.index(max(toubu))][0])
        xp.remove(xp[b.index(max(toubu))])
    else:
        print(xp[index_[0]][0])
        xp.remove(xp[index_[0]])