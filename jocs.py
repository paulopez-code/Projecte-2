from robot import robot
import random
def janken():
    opcions = ["pedra", "paper", "tisores"]
    while True:
        victoria = False
        dificultat = input("vols jugar al millor de 3 rondes o al millor de 5? (S/s per sortir) ")
        if dificultat == "S" or dificultat == "s":
            print("Fins la propera!")
            break
        rondes_usuari = 0
        rondes_maquina = 0
        if dificultat not in ["3","5"]:
            print("opció no vàlida, torna-ho a intentar")
        elif dificultat == "3":
            while not victoria:
                eleccio = input("Escull pedra, paper o tisores (S/s per sortir): ")
                eleccio_maquina = robot().playing()
                if eleccio not in opcions:
                    print("Elecció no vàlida. Torna-ho a intentar.")
                if eleccio == eleccio_maquina:
                    print("Empat")
                if (eleccio == "pedra" and eleccio_maquina == "tisores"):
                    print("Felicitats, has guanyat!")
                    rondes_usuari += 1
                if (eleccio == "paper" and eleccio_maquina == "pedra"):
                    print("Felicitats, has guanyat!")
                    rondes_usuari += 1
                if (eleccio == "tisores" and eleccio_maquina == "paper"):
                    print("Felicitats, has guanyat!")
                    rondes_usuari += 1
                if (eleccio == "pedra" and eleccio_maquina == "paper"):
                    print("Has perdut! La màquina ha escollit", eleccio_maquina)
                    rondes_maquina += 1
                if (eleccio == "paper" and eleccio_maquina == "tisores"):
                    print("Has perdut! La màquina ha escollit", eleccio_maquina)
                    rondes_maquina += 1
                if (eleccio == "tisores" and eleccio_maquina == "pedra"):
                    print("Has perdut! La màquina ha escollit", eleccio_maquina)
                    rondes_maquina += 1
                if eleccio == "S" or eleccio == "s":
                    print("Fins la propera!")
                    break
                if rondes_usuari == 3:
                    print("Enhorabona! Has guanyat la partida!")
                    victoria = True
                if rondes_maquina == 3:
                    print("La màquina ha guanyat la partida. Millor sort la pròxima vegada!")
                    victoria = True
        elif dificultat == "5":
            while not victoria:
                eleccio = input("Escull pedra, paper o tisores (S/s per sortir): ")
                eleccio_maquina = robot().playing()
                if eleccio not in opcions:
                    print("Elecció no vàlida. Torna-ho a intentar.")
                if eleccio == eleccio_maquina:
                    print("Empat")
                if (eleccio == "pedra" and eleccio_maquina == "tisores"):
                    print("Felicitats, has guanyat!")
                    rondes_usuari += 1
                if (eleccio == "paper" and eleccio_maquina == "pedra"):
                    print("Felicitats, has guanyat!")
                    rondes_usuari += 1
                if (eleccio == "tisores" and eleccio_maquina == "paper"):
                    print("Felicitats, has guanyat!")
                    rondes_usuari += 1
                if (eleccio == "pedra" and eleccio_maquina == "paper"):
                    print("Has perdut! La màquina ha escollit", eleccio_maquina)
                    rondes_maquina += 1
                if (eleccio == "paper" and eleccio_maquina == "tisores"):
                    print("Has perdut! La màquina ha escollit", eleccio_maquina)
                    rondes_maquina += 1
                if (eleccio == "tisores" and eleccio_maquina == "pedra"):
                    print("Has perdut! La màquina ha escollit", eleccio_maquina)
                    rondes_maquina += 1
                if eleccio == "S" or eleccio == "s":
                    print("Fins la propera!")
                    break
                if rondes_usuari == 5:
                    print("Enhorabona! Has guanyat la partida!")
                    victoria = True
                if rondes_maquina == 5:
                    print("La màquina ha guanyat la partida. Millor sort la pròxima vegada!")
                    victoria = True
def nana():
    Nombre_escollit = random.randint(1, 100)
    cont = 0
    endevinat = False
    while not endevinat:
        Nombre = input("Digues un nombre de l'1 al 100, o S/s per sortir: ")
        if Nombre == 's' or Nombre == 'S':
            print("has sortit del joc")
            break
        Nombre_int = int(Nombre)
        cont += 1
        if Nombre_int < 1 or Nombre_int > 100:
            print("Si us plau, introdueix un nombre de l'1 al 100.")
            continue
        if Nombre_int < Nombre_escollit:
            print("el nombre es massa petit")
        if Nombre_int > Nombre_escollit:
            print("el nombre es massa gran")
        if Nombre_int == Nombre_escollit:
            print("Felicitats! Has encertat el nombre en", cont, "intents")
            endevinat = True
        if not Nombre.isdigit():
            print("Si us plau, introdueix un nombre vàlid.")
if __name__ == "__main__":
    janken()
    nana()