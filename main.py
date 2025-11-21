from jocs import janken as janken_game, nana as nana_game
from time import sleep
def main():
    while True:
        print("--Benvingut/da al miniarcade!--")
        print("1. Pedra, paper, tisores")
        print("2. Endevina el nombre")
        print("S/s Sortir")
        joc = input("Tria un joc o surt: ")
        if joc == "1":
            janken_game()
            sleep(3)
        elif joc == "2":
            nana_game()
            sleep(3)
        elif joc in ("S", "s"):
            print("Fins la proxima! Esperem que t'ho hagis passat bé!")
            break
        else:
            print("Opció no vàlida. Introdueix una vàlida.")
            sleep(3)


if __name__ == "__main__":
    main()