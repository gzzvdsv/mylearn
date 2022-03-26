# 位置参数>*args>默认值参数(关键字参数)>**kwargs
def chuacas(a, b='a', c='a'):
    print(a, 'b:,',b, 'c:',c)


chuacas('a', 'asd', 'xcv')
# 关键字参数
def chuancan(a,b,c,*args,d=None,e=None,**kwargs):
    print(a,b,c,args,d,e,kwargs)
    # print(type(**kwargs))
chuancan('a','b','c',d='d',e='e',f='xzcv')