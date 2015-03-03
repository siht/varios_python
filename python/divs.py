def meth1(lst, divs):
    c = 0
    size = len(divs)
    for i in lst:
        while c < size and not i % divs[c]:
            c += 1
        if c == size:
            # print i
            pass
        c = 0

def meth2(lst, divs):
    for item in lst:
        if all([item % i == 0 for i in divs]):
            # print item
            pass

def meth3(lst, divs):
    for i in lst:
        for j in divs:
            if i%j != 0: break
        else:
            # print i
            pass

def main():
    import time
    x = xrange(1,5000)
    divs = xrange(1,11)
    
    t1 = time.clock()
    meth1(x, divs)
    t1 = time.clock() - t1
    
    t2 = time.clock()
    meth2(x, divs)
    t2 = time.clock() - t2
    
    t3 = time.clock()
    meth3(x, divs)
    t3 = time.clock() - t3
    
    print 'tiempo de ejecucion de la funcion 1:', t1
    print 'tiempo de ejecucion de la funcion 2:', t2
    print 'tiempo de ejecucion de la funcion 3:', t3
    
if __name__ == '__main__':
    main()