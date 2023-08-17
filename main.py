import math

def sumacmpl(cplx1, cplx2):
    numR = cplx1[0] + cplx2[0]
    numI = cplx1[1] + cplx2[1]
    sumcplx = [numR, numI]
    return sumcplx
def restacmpl(cplx1, cplx2):
    numR = cplx1[0] - cplx2[0]
    numI = cplx1[1] - cplx2[1]
    rescplx = [numR, numI]
    return rescplx
def multcmpl(cplx1, cplx2):
    multR = cplx1[0]*cplx2[0] - cplx1[1]*cplx2[1]
    multI = cplx1[0]*cplx2[1] + cplx1[1]*cplx2[0]
    multcplx = [multR, multI]
    return multcplx
def divcmpl(cplx1, cplx2):
    MultIzq = cplx1[0]*cplx2[0] + cplx1[1]*cplx2[1]
    MultDer = cplx1[0]*cplx2[0] - cplx1[1]*cplx2[1]
    Divisor = cplx2[0]**2 + cplx2[1]**2
    return (MultIzq/Divisor , MultDer/Divisor)
def conjcmpl(cplx):
    cplx[1] = cplx[1]*-1
    return cplx

def modcmpl(cplx):
    mod = ((cplx[0]**2) + (cplx[1]**2))**(1/2)
    return mod
def fasecmpl(cplx):
    numR = cplx[0]
    numI = cplx[1]
    fase = math.atan(numI/numR)
    return fase
def convCarToPol(cplx):
    val1 = modcmpl(cplx)
    val2 = fasecmpl(cplx)
    polar = [val1, val2]
    return polar
def convPolToCar(cplx):
    val1 = cplx[0]*math.cos(cplx[1])
    val2 = cplx[0]*math.sin(cplx[1])
    car = [val1, val2]
    return car

def printer(cplx):
    print(str(cplx[0]) + "+" + "(" + str(cplx[1]) + ")" + "i")

def printerPol(cplx):
    print(str(cplx[0]) + "(" + "Cos" + str(cplx[1]) + "+" + "i"+ "(" + "Sen" + str(cplx[1]) + ")")

def printerReal(Num):
    print(Num)