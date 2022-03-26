lis_ = [2, 3, 4,5]
ne_lis = [[2], []]
while len(lis_) != 0:
    for i in range(len(ne_lis)):
        if  len(lis_) == 0:
            break
        print("i--", i)
        if i>0:
            z=i-1
        else:
            z=i
        if min(lis_) % ne_lis[z][0] == 0:
            ne_lis[i].append(min(lis_))
            lis_.remove(min(lis_))
            print("ne_lis--", ne_lis)
            print("lis_--", lis_)
            break
        else:
            # if ne_lis
            ne_lis[i+1].append(min(lis_))
            lis_.remove(min(lis_))
            print("ne_lis--", ne_lis)
            print("lis_--", lis_)
while len(lis_) == 0:
    print("color",len(ne_lis))
    break