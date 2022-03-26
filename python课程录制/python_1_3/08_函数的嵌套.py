def func1(a):
    print('func1执行')
    def  func2():
        print('func2执行')
    print('func1执行结束',a,'次')
    func2()
    if a<100:
        a+=1
        func1(a)
func1(0)