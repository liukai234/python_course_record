import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a != 0:
    delta = math.pow(b, 2)-4*a*c
    if delta < 0:
        print("无解")
    elif delta == 0:
        s = -b/(2*a)
        print("一个解x =",s)
    else :
        root = math.sqrt(delta)
        x1 = (-b+root)/(2*a)
        x2 = (-b-root)/(2*a)
        print("x1=",x1,"\t","x2=",x2)
