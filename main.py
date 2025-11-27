import jocs
from time import sleep
def main():
    while True:
        print("--Benvingut/da al miniarcade!--")
        print("1. Pedra, paper, tisores")
        print("2. Endevina el nombre")
        print("S/s Sortir")
        joc = input("Tria un joc o surt: ")
        match joc:
            case '1':
                jocs.janken()
                sleep(3)
            case '2':
                jocs.nana()
                sleep(3)
            case 'S' | 's':
                print("Fins la proxima! Esperem que t'ho hagis passat bé!")
                break
            case _:
                print("Opció no vàlida. Introdueix una vàlida.")
                sleep(3)


if __name__ == "__main__":
    main()