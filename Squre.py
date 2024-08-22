import math

def S (x,y,z):
    return math.sqrt(((x+y+z)/2)*((x+y+z)/2-x)*((x+y+z)/2-y)*((x+y+z)/2-z))
a=float(input("第一条边="))
b=float(input("第二条边="))
c=float(input("第三条边="))
print(S(a,b,c))