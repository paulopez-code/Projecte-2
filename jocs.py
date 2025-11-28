# importem robot de robot.py
import robot
# importem la llibreria random per a la generació de nombres aleatoris en la funció nana
import random
# Joc de pedra, paper o tisores contra la màquina
def janken():
    # Definim les opcions disponibles
    opcions = ["pedra", "paper", "tisores"]
    # Bucle principal del joc
    while True:
        # La variable victoria controla quan acaba el joc
        victoria = False
        # Preguntem la dificultat del joc segons el nombre de rondes: 3 o 5 rondes, més l'opció  de sortir
        dificultat = input("vols jugar al millor de 3 rondes o al millor de 5? (S/s per sortir) ")
        # Si l'usuari vol sortir, trenquem el bucle
        if dificultat == "S" or dificultat == "s":
            print("Fins la propera!")
            break
        # Inicialitzem els comptadors de rondes guanyades per a l'usuari i la maquina.
        rondes_usuari = 0
        rondes_maquina = 0
        # Comprovem que la dificultat sigui vàlida, sinó tornem a demanar-la
        if dificultat not in ["3","5"]:
            print("opció no vàlida, torna-ho a intentar")
        # Si la dificultat és de 3 rondes entrem a la partida amb les condicions corresponents
        if dificultat == "3":
            while not victoria:
                # Demanem l'elecció de l'usuari, revem la resposta de la maquina, i comprovem les possibles jugades i els reusltats corresponents
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
                # S'identifica si l'usuari vol sortir del joc, ha guanyat o ha perdut
                if eleccio == "S" or eleccio == "s":
                    print("Fins la propera!")
                    break
                if rondes_usuari == 3:
                    print("Enhorabona! Has guanyat la partida!")
                    victoria = True
                if rondes_maquina == 3:
                    print("La màquina ha guanyat la partida. Millor sort la pròxima vegada!")
                    victoria = True
        # Si la dificultat és de 5 rondes entrem a la partida
        if dificultat == "5":
            while not victoria:
                # Demanem l'elecció de l'usuari, activem la maquina, i comprovem les possibles jugades i els reusltats corresponents
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
                # S'identifica si l'usuari vol sortir del joc, ha guanyat o ha perdut
                if eleccio == "S" or eleccio == "s":
                    print("Fins la propera!")
                    break
                if rondes_usuari == 5:
                    print("Enhorabona! Has guanyat la partida!")
                    victoria = True
                if rondes_maquina == 5:
                    print("La màquina ha guanyat la partida. Millor sort la pròxima vegada!")
                    victoria = True
# Comencem la funcio del joc d'endevinar un nombre entre l'1 i el 100
def nana():
    # Generem un nombre aleatori entre l'1 i el 100
    Nombre_escollit = random.randint(1, 100)
    # El comptador d'intents s'inicia des de 0 en cada partida
    cont = 0
    # La variable endevinat controla quan acaba el joc
    endevinat = False
    while not endevinat:
        # Es pregunta a l'usuari si vol sortir, o que trii un nombre dintre de les possibles respostes
        Nombre = input("Digues un nombre de l'1 al 100, o S/s per sortir: ")
        # Si l'usuari vol sortir, trenquem el bucle
        if Nombre == 's' or Nombre == 'S':
            print("has sortit del joc")
            break
        # Convertim la resposta de l'usuari a enter per a poder comparar-la amb el nombre escollit i sumem un intent cada cop
        Nombre_int = int(Nombre)
        cont += 1
        # Comprovem si el nombre està dintre del rang permès
        if Nombre_int < 1 or Nombre_int > 100:
            print("Si us plau, introdueix un nombre de l'1 al 100.")
        # Comprovem si el nombre és massa petit, massa gran o el nombre es correcte
        if Nombre_int < Nombre_escollit:
            print("el nombre es massa petit")
        if Nombre_int > Nombre_escollit:
            print("el nombre es massa gran")
        if Nombre_int == Nombre_escollit:
            print("Felicitats! Has encertat el nombre en", cont, "intents")
            endevinat = True
        # Comprovem que l'entrada de l'usuari sigui un nombre vàlid
        if not Nombre.isdigit():
            print("Si us plau, introdueix un nombre vàlid.")
# Comencem la funció del joc de moneda
def moneda():
    # Definim les opcions disponibles i que la variable victoria sigui falsa
    opcions = ["cara", "creu", "S", "s"]
    victoria = False
    # Comencem el bucle principal del joc on l'usuari ha d'introduir la seva predicció
    while not victoria:
        eleccio = input("Escull cara o creu (S/s per sortir): ")
        # Activem la classe "moneda" de robot per a obtenir una elecció aleatòria
        eleccio_moneda = robot.moneda().playing()
        # Comprovem que l'elecció de l'usuari sigui vàlida, correcta, incorrecta o si vol sortir
        if eleccio not in opcions:
            print("Elecció no vàlida. Torna-ho a intentar.")
        if eleccio == eleccio_moneda:
            print("Felicitats, has guanyat! La moneda ha caigut en", eleccio_moneda)
            victoria = True
        if eleccio != eleccio_moneda:
            print("Has perdut! La moneda ha caigut en", eleccio_moneda)
        if eleccio == "S" or eleccio == "s":
            print("Fins la propera!")
            break
# Tanquem les funcions com a funcions principals de jocs.py per a poder ser utilitzades des de main.py més fàcilment
if __name__ == "__main__":
    janken()
    nana()
    moneda()