def palouti(n):
    a = 1
    b = 2
    temp = 0
    if (n == 1) or (n == 2):
        return n
    for i in range(3, n + 1):
        temp = a + b
        a = b
        b = temp
    return temp


print(palouti(10))
