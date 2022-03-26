import sys
import pandas

list,num =[],0
while num <= 100 :
    length = len(list)
    size = sys.getsizeof(list)
    print('length = '+str(length)+'  size = '+str(size) + ' -- ' + str(id(list)))
    list.append(None)
    num += 1

zp=pandas.DataFrame()