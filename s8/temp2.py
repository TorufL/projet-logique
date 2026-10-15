def addition(a, b):
    return a + b
print(addition(10,20))


addition2 = lambda a,b: a+b
print(addition2(20,6))

########################################################################
########################################################################
########################################################################

def division(a,b):
    return a/b
print(division(10,5))


division2 = lambda a,b: a/b
print(division2(20,5))

division_entiere = lambda n1,n2: n1 // n2
print(division_entiere(20,6))



choix = iter(["a", "b", "c"])
print(next(choix))
print(next(choix))
print(next(choix))