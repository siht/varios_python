def m_b1_pendiente(dic):
    par1 = 0.
    sumX = 0.
    sumY = 0.
    sumXquad = 0.
    for x,y in dic.items():
        par1 += x*y
        sumX += x
        sumY += y
        sumXquad += x**2
    num = par1 - sumX*sumY
    den = len(dic)*sumXquad - sumX**2
    return num/den
    
def mediaXY(dic):
    sumX = 0.
    sumY = 0.
    for x,y in dic.items():
        sumX += x
        sumY += y
    return sumX/len(dic), sumY/len(dic)
    
def origen_b0_punto(dic):
    mx,my = mediaXY(dic)
    return my - m_b1_pendiente(dic)*mx
    
def puntoPendiente_y_regLin(dic):
    b1=m_b1_pendiente(dic)
    b0=origen_b0_punto(dic)
    dout={}
    for x,y in dic.items():
        dout.update({x:b0+b1*x})
    return dout

if __name__ == '__main__':
    a = {23:230,26:255,30:228,33:330,34:229,43:430,40:420,42:420,50:500}
    b = puntoPendiente_y_regLin(a)
    r = regresionLineal2(a)
    ind = sorted(a)
    for i in ind:
        print i,'=',a[i]
    for i in ind:
        print i,'=',b[i]
    for i in ind:
        print i,'=',r[i]