# def func():
#     print('func执行了')
#     yield 'hello'
#
# z=func()
# print(z)
# print(z.__next__())
#



def func():
    print('func执行了1')
    yield 'hello'
    print('func执行了2')
    yield 'hello'
    print('func执行了3')
    yield 'hello'
    print('func执行了4')
    yield 'hello'

z=func()
print(z)
while 1:
    try:
        print(z.__next__())
    except:
        break

# 作用节省内存