# importem el fitxer jocs.py per a poder utilitzar les seves funcions en el menu
import jocs
# importem sleep per a posar pauses entre les diferents pantalles
from time import sleep
# generem la funció principal del miniarcade
def main():
    while True:
        # Mostrem el menu principal amb les opcions disponibles
        print("--Benvingut/da al miniarcade!--")
        print("1. Pedra, paper, tisores")
        print("2. Endevina el nombre")
        print("S/s Sortir")
        # Demanem a l'usuari que triï un joc o que surti del menu
        joc = input("Tria un joc o surt: ")
        # Utilitzem un match per a gestionar les diferents opcions del menu i entri a les funcions de jocs.py, surti o doni error
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
# acabem la funció com a funció principal
if __name__ == "__main__":
    main()