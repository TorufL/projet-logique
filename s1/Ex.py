# ex1
print("ex1")
dispo = (1000-673)
print("bande passante dispo:", dispo, "Mbps")
utilisation = (673*100/1000)
print("Pourcentage d'utilisation:", utilisation, "%")
print(" ")

#-----------------------------------------------------------------------------------------------------------------------

# ex2
print("ex2")
print("100Mbps=", 100/8, "MB/s")
print(" ")

print("500Mbps=", 500/8, "MB/s")
print(" ")

print("1000Mbps=", 1000/8, "MB/s")
print(" ")

#-----------------------------------------------------------------------------------------------------------------------

# ex3
print("ex3")

#taille du fichier en GB
t = (4.7)

#vitesse de téléchargmement
v = (50)

#formules
mb = (t * 1024)
print("taille du fichier:", mb, "MB")
mbs = (v/8)
print("vitess:", mbs, "MB/s")
temps = (mb/mbs)
print("temps en secondes:", temps, "s")
minutes = (temps/60)
print("temps en minutes:", minutes, "m")
print(" ")

#-----------------------------------------------------------------------------------------------------------------------

#ex4
p1 = (80)
p2 = (65535)
p3 = (70000)
p4 = (-5)
p5 = (22)

if p1 <= 65535 and >= 0:
    print("valide")
else:
    print("invalide")