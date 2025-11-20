from robot import robot
import random
def janken():
    opcions = ["pedra", "paper", "tisores"]
    while True:
        eleccio = input("Escull pedra, paper o tisores (S/s per sortir): ")
        eleccio_maquina = robot().playing()
        if eleccio == "S" or eleccio == "s":
            print("Fins la propera!")
            break
        elif eleccio not in opcions:
            print("Elecció no vàlida. Torna-ho a intentar.")
        elif eleccio == eleccio_maquina:
            print("Empat")
        elif (eleccio == "pedra" and eleccio_maquina == "tisores"):
            print("Felicitats, has guanyat!")
            break
        elif (eleccio == "paper" and eleccio_maquina == "pedra"):
            print("Felicitats, has guanyat!")
            break
        elif (eleccio == "tisores" and eleccio_maquina == "paper"):
            print("Felicitats, has guanyat!")
            break
        elif (eleccio == "pedra" and eleccio_maquina == "paper"):
            print("Has perdut! La màquina ha escollit", eleccio_maquina)
        elif (eleccio == "paper" and eleccio_maquina == "tisores"):
            print("Has perdut! La màquina ha escollit", eleccio_maquina)
        elif (eleccio == "tisores" and eleccio_maquina == "pedra"):
            print("Has perdut! La màquina ha escollit", eleccio_maquina)
janken()

def nana():
    Nombre_escollit = random.randint(1, 100)
    cont = 0
    endevinat = False
    while not endevinat:
        Nombre = input("Digues un nombre de l'1 al 100, o S/s per sortir: ")
        Nombre = int(Nombre)
        cont += 1
        if Nombre < Nombre_escollit:
            print ("el nombre es massa petit")
        elif Nombre > Nombre_escollit:
            print ("el nombre es massa gran")
        elif Nombre == Nombre_escollit:
            print ("Felicitats! Has encertat el nombre en", cont, "intents")
            endevinat = True
        elif Nombre == "S" | Nombre == "s":
            print ("has sortit del joc")
            break
        else:
            print ("Si us plau, introdueix un nombre vàlid.")
nana()