while True:
    print("--Benvingut/da al miniarcade!--")
    print("1. Pedra, paper, tisores")
    print("2. Endevina el nombre")
    print("S/s Sortir")
    joc = input("Tria un joc o surt: ")
    if joc == "1":
        from jocs import janken
    elif joc == "2":
        from jocs import nana
    elif joc == "s" or joc == "S":
        print("Fins la proxima! Esperem que t'ho hagis passat bé!")
        break