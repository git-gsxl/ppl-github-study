
# 类
class Count(object):

    # 方法
    def add(self, a=0, b=0):
        return a+b

    def acc(self, a, b):
        e = a-b
        return e

    def axx(self, a, b):
        # （a+b）*(a-b)
        self.add(a, b)*self.acc(a, b)

# 继承上面Count类
class jicheng(Count):
    def sanlou(self, a, b):
        return "第三层"

    # 覆盖上面Count类的add方法
    def add(self, a=0, b=0):
        return "覆盖"

if __name__ == '__main__':
    # 实例化
    a = Count()
    a.acc()
    a.add()