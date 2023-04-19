from math import sqrt


a = float(input("a"))
b = float(input("b"))
c = float(input("c"))
delta= (b)**2-4*a*c
print (delta)

if delta <0 :
    print("Il existe 0 racines")
    print ( str(abs(a)/a)[0])
elif delta ==0 :
    r1 = (-b/(2*a))
    print("Il existe 1 racines:", r1 )
    print ( str(abs(a)/a)[0], "|>" , r1 , "<|", str(abs(a)/a)[0])
else :
    a1 = (-b+ sqrt(delta))/(2*a)
    a2 = (-b- sqrt(delta)) /(2*a)

    if a1 > a2:
        r1 = a2
        r2 = a1
    else:
        r2 = a2
        r1 = a1

    print("Il existe 2 racines:", r1 ,"et", r2) 
    print ( str(abs(a)/a)[0], "|>", r1, "<|", str(abs(a)/-a)[0] , "|>", r2, "<|", str(abs(a)/a)[0] )