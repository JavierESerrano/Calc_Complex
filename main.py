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
def conjcmpl(cplx):
    cplx[1] = cplx[1]*-1
    return cplx
def divcmpl(cplx1, cplx2):
    conj = conjcmpl(cplx2)
    multUp = multcmpl(cplx1, conj)
    multDw = multcmpl(cplx2, conj)
    divR = multUp[0]/multDw[0]
    divI = multUp[1]/multDw[1]
    divCplx = [divR, divI]
    return divCplx
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

print("suma")
printer(sumacmpl([2,3],[1,5]))
print("resta")
printer(restacmpl([2,3],[1,5]))
print("multiplicacion")
printer(multcmpl([2,3],[1,5]))
print("division")
printer(divcmpl([2,3],[1,5]))
print("conjugado")
printer(conjcmpl([5,-6]))
print("modulo")
printerReal(modcmpl([-1,-9]))
print("fase")
printerReal(fasecmpl([-2,5]))
print("conversion de cartesianas a polares")
printerPol(convCarToPol([6,5]))
print("conversion de polares a cartesianas")
printer(convPolToCar([2,4]))