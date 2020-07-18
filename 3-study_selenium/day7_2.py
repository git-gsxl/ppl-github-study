# 类
class CountAdd(object):

    def __init__(self, x, y):   # 初始化
        self.a = x
        self.b = y
        self.f = self.add()

    # 方法
    def add(self, a=0, b=0):
        return self.a + self.b

    def acc(self):
        e = self.a - self.b
        return e

    def axx(self):
        # （a+b）*(a-b)
        return self.add()*self.acc()

if __name__ == '__main__':
    # 实例化
    q = CountAdd(4, 6)   # 传参，默认参数
    print(q.a)
    print(q.add())
    print(q.f)

