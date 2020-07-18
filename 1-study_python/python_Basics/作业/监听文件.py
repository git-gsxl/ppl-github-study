def tail(filename):
    f = open(filename, encoding='utf-8')
    while 1:
        line = f.readline()
        q = line.strip()
        if q:
            yield q

g = tail('file')
for i in g:
    # if i == 'python':
    print(i)

