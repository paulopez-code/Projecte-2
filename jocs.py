from robot import robot
import random
def janken():
    opcions = ["pedra", "paper", "tisores"]
    while True:
        dificultat = input("vols jugar al millor de 3 rondes o al millor de 5? (S/s per sortir) ")
        if dificultat == "S" or dificultat == "s":
            print("Fins la propera!")
            break
        rondes_usuari = 0
        rondes_maquina = 0
        if dificultat not in ["3","5"]:
            print("opció no vàlida, torna-ho a intentar")
            continue
        elif dificultat == "3":
            while rondes_usuari < 4 and rondes_maquina < 4:
                eleccio = input("Escull pedra, paper o tisores (S/s per sortir): ")
                eleccio_maquina = robot().playing()
                if eleccio not in opcions:
                    print("Elecció no vàlida. Torna-ho a intentar.")
                elif eleccio == eleccio_maquina:
                    print("Empat")
                elif (eleccio == "pedra" and eleccio_maquina == "tisores"):
                    print("Felicitats, has guanyat!")
                    rondes_usuari += 1
                elif (eleccio == "paper" and eleccio_maquina == "pedra"):
                    print("Felicitats, has guanyat!")
                    rondes_usuari += 1
                elif (eleccio == "tisores" and eleccio_maquina == "paper"):
                    print("Felicitats, has guanyat!")
                    rondes_usuari += 1
                elif (eleccio == "pedra" and eleccio_maquina == "paper"):
                    print("Has perdut! La màquina ha escollit", eleccio_maquina)
                    rondes_maquina += 1
                elif (eleccio == "paper" and eleccio_maquina == "tisores"):
                    print("Has perdut! La màquina ha escollit", eleccio_maquina)
                    rondes_maquina += 1
                elif (eleccio == "tisores" and eleccio_maquina == "pedra"):
                    print("Has perdut! La màquina ha escollit", eleccio_maquina)
                    rondes_maquina += 1
                elif eleccio == "S" or eleccio == "s":
                    print("Fins la propera!")
                    break
                elif rondes_usuari == 3:
                    print("Enhorabona! Has guanyat la partida!")
                    break
                elif rondes_maquina == 3:
                    print("La màquina ha guanyat la partida. Millor sort la pròxima vegada!")
                    break
        elif dificultat == "5":
            while rondes_usuari < 6 and rondes_maquina < 6:
                eleccio = input("Escull pedra, paper o tisores (S/s per sortir): ")
                eleccio_maquina = robot().playing()
                if eleccio not in opcions:
                    print("Elecció no vàlida. Torna-ho a intentar.")
                elif eleccio == eleccio_maquina:
                    print("Empat")
                elif (eleccio == "pedra" and eleccio_maquina == "tisores"):
                    print("Felicitats, has guanyat!")
                    rondes_usuari += 1
                elif (eleccio == "paper" and eleccio_maquina == "pedra"):
                    print("Felicitats, has guanyat!")
                    rondes_usuari += 1
                elif (eleccio == "tisores" and eleccio_maquina == "paper"):
                    print("Felicitats, has guanyat!")
                    rondes_usuari += 1
                elif (eleccio == "pedra" and eleccio_maquina == "paper"):
                    print("Has perdut! La màquina ha escollit", eleccio_maquina)
                    rondes_maquina += 1
                elif (eleccio == "paper" and eleccio_maquina == "tisores"):
                    print("Has perdut! La màquina ha escollit", eleccio_maquina)
                    rondes_maquina += 1
                elif (eleccio == "tisores" and eleccio_maquina == "pedra"):
                    print("Has perdut! La màquina ha escollit", eleccio_maquina)
                    rondes_maquina += 1
                elif eleccio == "S" or eleccio == "s":
                    print("Fins la propera!")
                    break
                elif rondes_usuari == 5:
                    print("Enhorabona! Has guanyat la partida!")
                    break
                elif rondes_maquina == 5:
                    print("La màquina ha guanyat la partida. Millor sort la pròxima vegada!")
                    break
def nana():
    Nombre_escollit = random.randint(1, 100)
    cont = 0
    endevinat = False
    while not endevinat:
        Nombre = input("Digues un nombre de l'1 al 100, o S/s per sortir: ")
        if Nombre in ("S", "s"):
            print("has sortit del joc")
            break
        try:
            Nombre_int = int(Nombre)
        except ValueError:
            print("Si us plau, introdueix un nombre vàlid.")
            continue
        cont += 1
        if Nombre_int < Nombre_escollit:
            print("el nombre es massa petit")
        elif Nombre_int > Nombre_escollit:
            print("el nombre es massa gran")
        else:
            print("Felicitats! Has encertat el nombre en", cont, "intents")
            endevinat = True


if __name__ == "__main__":
    janken()
    nana()