class car:
    def __init__(self, color, pai, pailiang):
        self.color = color
        self.pai = pai
        self.pail = pailiang
    # 跑 动作 功能 ->函数
    # 在类中写入的函数->方法
    def pao(self):
        print('我的车能跑是%s的车牌号%s排量是%s' % (self.color, self.pai, self.pail))


c1 = car('红色', 'B231', 12) #创建car对象此时的self参数不需要我们去管
c2 = car('蓝色', 'B555', 11)
print(c1.color)
print(c2.color)
c1.pao()
c2.pao()



class Car:  #类名首字母大写，严格遵守驼峰规则
    #__init__方法是一个特殊的方法  初始化方法（构造方法）
    #在创建对象的时候会自动调用__init__()
    # self 就是你创建出来的对象
    def __init__(self):
        # init 初始化方法在创建对象的时候默认执行这个函数
        print()

