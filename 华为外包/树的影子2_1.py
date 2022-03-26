num=int(input())
list_ = input().split()
for i in range(len(list_)):
    list_[i]=int(list_[i])
al_=0
for i in range(len(list_)-1):
    if (list_[i]+list_[i+1])>=100:
        pass
    else:
        print(list_[i] + list_[i + 1])
        al_+=100-(list_[i] + list_[i + 1])
print(al_)