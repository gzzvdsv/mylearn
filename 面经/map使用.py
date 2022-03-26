# a=[1,2,4,5,62,5,6,8,45,45,78,32]
# def func(x):
#     if x<10:
#         return True
#     else:
#         return False
# zp=list(map(func,a))
# print(zp)


def is_odd(n):
    # return n % 2 == 1
    return n>7


tmplist = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(tmplist)