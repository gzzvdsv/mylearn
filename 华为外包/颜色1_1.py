num_=4
lis_=[2,4,6,8]
colo_=0
ne_lis=[[],[],[],[],[],[],[],[],[],[],[]]
ne_lis[0].append(min(lis_))
lis_.remove(min(lis_))
for i in range(num_):
    print(max(lis_))
    print(min(lis_))
while len(lis_)!=0:
    for i in len(ne_lis):
        if min(lis_) % ne_lis[i][0]==0:
            ne_lis[i].append(min(lis_))
            lis_.remove(min(lis_))
            break
        else:
            pass
    pass