#  测试 LEGB
str = "global"

def outer():
    # str = "outer()"
    print(str)

    def inner():
        str = "inner()"
        print(str)
    inner()

outer()
