l = "="*10


#arithmétiques

r1 = 8*(4*3+12-5*3)+8*33/2*32
print(r1)
print(l)
r2 = (2*5+3)*(2*5+1)+((5+7)*(2*5+1))/2
print(r2)
print(l)

#logique

r3 = 3>19 and 5<4 or 18<15 and 6>4
print(r3)
print(l)
r4 = 3>19 or (13>2 and (5<4 or 18<15 and 7>4))
print(r4)
print(l)

#comparaisons

a = 2
b = 9
c = 5

r5 = a + (b*2)>15 or c-3<2
print(r5)
print(l)

r6 = not(b/3<a+1) and (c*2==10)
print(r6)
print(l)

r7 = (a + c > b) and (b-5<c or a*3==6)
print(r7)
print(l)

r8 = not(a**2+b>12) or (c+3<=b and a<c)
print(r8)
print(l)

#Analyse

A=4
B=8

r9 = 3+B>19-A or 5<4 and 18<15 or 7>4
print(r9)
print(l)

#Partie 2

print("2+3= ", 2+3)