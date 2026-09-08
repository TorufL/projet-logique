
#nb d'étages
n = 10

for i in range(1, n+1):
    #espaces
    for j in range(n-i):
        print(" ", end=" ")
    #étoiles
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()