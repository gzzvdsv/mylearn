# 这个需要注意一下 里面的lis有时候不传会导致一直使用一个lis
def  func(var,lis=[]):
    lis.append(var)
    print(id(lis))
    print(lis)
func(111)
lis=[]
print(id(lis))
func(222,lis)