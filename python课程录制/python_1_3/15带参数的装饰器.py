def wapper_out(name):
    def wapper(fn):
        def inner(*args, **kwargs):
            print(f'我要开{name}')
            res = fn(*args, **kwargs)
            print('外挂关闭')
            print('==============================')
            return res

        return inner

    return wapper


@wapper_out('lol外挂')
def lol():
    print('lol大杀四方')


@wapper_out('dnf外挂')
def dnf():
    print('dnf秒杀卢克')


lol()
dnf()
