
def avg_func():
    cunt = 0
    sum = 0
    avg = 0
    while 1:
        num = yield avg
        sum += num
        cunt += 1
        avg = sum/cunt
        print(sum, cunt)

g = avg_func()
g.__next__()
avg = g.send(10)
avg = g.send(20)
avg = g.send(30)
avg = g.send(8)
print(avg)
