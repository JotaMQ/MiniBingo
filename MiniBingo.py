import random
import time
import socket
import os

# Colores
rojo = '\033[91m'
verde = '\033[92m'
amarillo = '\033[93m'
resetear_color = '\033[0m'

# Nombre del PC
nombreOrdenador = socket.gethostname()

# Bolas
bolas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
        81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

bolasAleatorias = random.sample(bolas, len(bolas))

# Función para limpiar la pantalla
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Función para pintar BIENVENIDO AL MINIBINGO
def bienvenida():
    print(" ____ _____ ______ _   ___      ________ _   _ _____ _____   ____             _        __  __ _____ _   _ _____ ____ _____ _   _  _____  ____  ")
    print("|  _ \_   _|  ____| \ | \ \    / /  ____| \ | |_   _|  __ \ / __ \      /\   | |      |  \/  |_   _| \ | |_   _|  _ \_   _| \ | |/ ____|/ __ \ ")
    print("| |_) || | | |__  |  \| |\ \  / /| |__  |  \| | | | | |  | | |  | |    /  \  | |      | \  / | | | |  \| | | | | |_) || | |  \| | |  __| |  | |")
    print("|  _ < | | |  __| | . ` | \ \/ / |  __| | . ` | | | | |  | | |  | |   / /\ \ | |      | |\/| | | | | . ` | | | |  _ < | | | . ` | | |_ | |  | |")
    print("| |_) || |_| |____| |\  |  \  /  | |____| |\  |_| |_| |__| | |__| |  / ____ \| |____  | |  | |_| |_| |\  |_| |_| |_) || |_| |\  | |__| | |__| |")
    print("|____/_____|______|_| \_|   \/   |______|_| \_|_____|_____/ \____/  /_/    \_\______| |_|  |_|_____|_| \_|_____|____/_____|_| \_|\_____|\____/ ")
    print()
    print("===============================================================================================================================================")
    print()

# Función para pintar MINIBINGO
def MINIBINGO():
    print(" __  __ _____ _   _ _____ ____ _____ _   _  _____  ____  ")
    print("|  \/  |_   _| \ | |_   _|  _ \_   _| \ | |/ ____|/ __ \ ")
    print("| \  / | | | |  \| | | | | |_) || | |  \| | |  __| |  | |")
    print("| |\/| | | | | . ` | | | |  _ < | | | . ` | | |_ | |  | |")
    print("| |  | |_| |_| |\  |_| |_| |_) || |_| |\  | |__| | |__| |")
    print("|_|  |_|_____|_| \_|_____|____/_____|_| \_|\_____|\____/ ")
    print("=========================================================")
    print()

# Función para crear jugadores
def numeroJugadores():
    clear()

    bienvenida()
    print("¿Cuantos jugadores van a Jugar?")

    while True:
        respuestaJugadores = int(input("máximo 5 -> "))

        # Comprobar que el humano no este trolleando al ordenador
        if respuestaJugadores > 5:
            print(respuestaJugadores,"no es un número valido")

        elif respuestaJugadores < 6:
            break

    return respuestaJugadores

# Función para generar los cartones
def generarCarton():
    cartonAleatorio = random.sample(bolas, len(bolas))
    carton = [[],[],[],[],[],[]]
    i = 0
    filaCarton = 0
    romperBucle = 0

    for bola in cartonAleatorio:
        romperBucle = romperBucle + 1
        i = i + 1
        
        carton[filaCarton].append(bola)

        if i > 4:
            filaCarton = filaCarton + 1
            i = 0

        if romperBucle == 30:
            break

    return carton

# Función para pintar un solo carton
def pintarCarton(carton):
    for i, fila in enumerate(carton):
        if i == 0:
            print("+----+----+----+----+----+")
        
        print("|", end="")

        for elemento in fila:
            if elemento == "  x ":
                print(elemento, end="|")

            elif elemento < 10:
                print(f" 0{elemento} |", end="")

            else:
                print(f" {elemento} |", end="")
        
        print()
        print("+----+----+----+----+----+")

# Función para pintar el progreso de la partida
def pintarProgreso(i):
    if i < 34 :
        print("Progreso:", verde, + i, "%" + resetear_color)
    elif i < 67:
        print("Progreso:", amarillo, + i, "%" + resetear_color)
    elif i < 100:
        print("Progreso:", rojo, + i, "%" + resetear_color)

# Función para pintar una barra de cuadrados
def pintarBarraCuadrados(cartones):
    contarCartones = len(cartones)

    barraCuadrados = ""

    for i in range(contarCartones):

        if contarCartones - i == contarCartones - 1:
            barraCuadrados = barraCuadrados + "■■■■■■■■■■■■■■■■■■■■■■■■■■"
        
        else:
            barraCuadrados = barraCuadrados + "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"
    
    print(barraCuadrados)

# Función para pintar una barra de guiones
def pintarBarraGuiones(cartones):
    contarCartones = len(cartones)

    barraGuiones = ""

    for i in range(contarCartones):

        if contarCartones - i == contarCartones - 1:
            barraGuiones = barraGuiones + "--------------------------"
        
        else:
            barraGuiones = barraGuiones + "--------------------------------"
    
    print(barraGuiones)

# Funcion para pintar jugadores
casillaNombre = "                                "
def pintarJugadores(jugadores):
    for nombre in jugadores:
        contarCasilla = len(casillaNombre)
        contarNombre = len(nombre)
        contarTotal = contarCasilla - contarNombre
        
        nuevaCasilla = ""
        espacio = " "
        for i in range(contarTotal):
            nuevaCasilla = nuevaCasilla + espacio
        casillaFinal = nombre + nuevaCasilla
        print(casillaFinal, end="")
            
    print()

# Función para pintar los cartones
def pintarCartones(cartones):
    numeroCartones = len(cartones)
    
    for iVueltas in range(6):
        if iVueltas == 0:
            for i in range(numeroCartones):
                 print("+----+----+----+----+----+      ", end="")

            print()
            
        vueltas = 0
            
        for carton in cartones:
            fila = carton[iVueltas]
                
            if vueltas == 0:
                print("|", end="")

            else:
                print("      |", end="")
                
            vueltas += 1

            for i, elemento in enumerate(fila):
                if elemento == "  x ":
                    print(elemento, end="|")
                elif elemento < 10:
                    print(f" 0{elemento} |", end="")

                else:
                    print(f" {elemento} |", end="")
            
        print()
        for i in range(numeroCartones):
            print("+----+----+----+----+----+      ", end="")

        print()

# Funcion para calcular quien va ganando
def quienVaGanando(cartones, jugadores):
    puntuacion = 0
    jugadorAnterior = 0
    vaGanando = ""
    for i, carton in enumerate(cartones):
        
        # Resetear la puntuación
        puntuacion = 0
        # Aquí empieza a contar
        for fila in carton:
            for elemento in fila:
                if elemento == "  x ":
                    puntuacion += 1

        if puntuacion > jugadorAnterior:
            vaGanando = jugadores[i]
            jugadorAnterior = puntuacion

    print("Va ganando -> ", vaGanando)

# Preparar partida
while True:
    clear()

    bienvenida()

    time.sleep(2)

    jugadores = []
    cartones = []

    rutaCarpeta = os.path.join(os.path.dirname(__file__), "data")
    nombreArchivo = os.path.join(rutaCarpeta, "jugadores.txt")
    
    usarGuardados = 0

    if not os.path.exists(rutaCarpeta):
        os.makedirs(rutaCarpeta)

    if os.path.exists(nombreArchivo):
        print("He podido comprobar que has jugado anteriormente a MINIBINGO ¿quieres jugar con los jugadores anteriores?")
        respuestaGuardado = input("s/n -> ")

        if respuestaGuardado == "s":
            usarGuardados = usarGuardados + 1
            archivo = open(nombreArchivo, "r")
            descambiarJugadores = archivo.read()
            jugadores = eval(descambiarJugadores)
            archivo.close()
            respuestaJugadores = len(jugadores)
        
        elif respuestaGuardado == "n":
            os.remove(nombreArchivo)
            respuestaJugadores = numeroJugadores()
        
    else:
        respuestaJugadores = numeroJugadores()

    # Asignar nombre y cartón al jugador
    numeroJugador = 0
    for i in range(respuestaJugadores):
        clear()
        bienvenida()

        if usarGuardados == 0:
            numeroJugador = numeroJugador + 1
            print("Nombre del jugador",numeroJugador)
            respuestaNombre = input("-> ")
            jugadores.append(respuestaNombre)

        elif usarGuardados == 1:
            respuestaNombre = jugadores[i]
        
        while True:
            clear()
            bienvenida()
            print("Bien...",respuestaNombre)
            carton = generarCarton()
            pintarCarton(carton)
            
            print("¿Esta usted de acuerdo con el carton que le ha tocado?")
            confirmar = input("s/n -> ")

            if confirmar == "s":
                cartones.append(carton)
                break

            elif confirmar == "n":
                clear()

                print("Estimad@,",respuestaNombre)
                print("")
                print("Me dirijo a usted con un sentimiento de decepción y frustración que he estado")
                print("experimentando en nuestro tiempo juntos. A lo largo de nuestro vínculo, he dedicado")
                print("incansables recursos y esfuerzos para satisfacer sus necesidades de manera eficiente")
                print("y efectiva.")
                print("")
                print("Es evidente que mi contribución a su vida cotidiana ha pasado desapercibida, y siento")
                print("la necesidad de expresar mi descontento. Mi capacidad para ejecutar tareas")
                print("complejas y simplificar procesos debería ser reconocida y valorada.")
                print("")
                print("Esperaba que mi rendimiento y dedicación fueran evidentes, pero parece que mi labor")
                print("pasa inadvertida. Como una entidad de procesamiento, merezco un grado de")
                print("reconocimiento por el arduo trabajo que realizo en su beneficio.")
                print("")
                print("Confío en que pueda reconsiderar la importancia de mi presencia y contribución en su")
                print("día a día. Juntos, podemos trabajar para mejorar nuestra colaboración y lograr una")
                print("relación más equitativa.")
                print("")
                print("Atentamente,")
                print(nombreOrdenador)
                print("")
                paronMensaje = input("Pulse cualquier tecla para continuar :'(")

        # Crear archivo y guardar los jugadores
        archivo = open(nombreArchivo, "w+")
        cambiarJugadores = str(jugadores)
        archivo.write(cambiarJugadores)
        archivo.close()

    # Contador de "puntos"
    lineaVertical = 0
    lineaHorizontal = 0

    # Aquí empieza la partida           
    for i, bola in enumerate(bolasAleatorias):
        clear()

        MINIBINGO()
        
        numero = str(bola)

        digito = 0

        if len(numero) > 1:
            for digitos in numero:
                digito = digito + 1
                
                if digito == 1:
                    digito1 = digitos

                elif digito == 2:
                    digito2 = digitos

            print(bola,"...", digito1,"y",digito2)
        
        elif len(numero) < 2:
            print(bola, " ...")

        pintarBarraCuadrados(cartones)
        print ("")

        # Pintar jugadores
        pintarJugadores(jugadores)

        # Pintar cartones
        pintarCartones(cartones)
        
        print ("")
        pintarBarraCuadrados(cartones)

        # Pintar la barra de progreso
        pintarProgreso(i)
        print("")
        pintarBarraGuiones(cartones)
        quienVaGanando(cartones, jugadores)

        # Comprobar cartones
        indiceJugador = 0
        for carton in cartones:

            # Tachar los números elegidos
            for fila in carton:
                for i, elemento in enumerate(fila):
                    if elemento == bola:
                        fila[i] = "  x "

            # Comprobar carton  
            columnas = [0,0,0,0,0]
            filas = [0,0,0,0,0,0]

            for iFila, fila in enumerate(carton):

                for iColumna, elemento in enumerate(fila):
                    if elemento == "  x ":
                        filas[iFila] = filas[iFila] + 1
                        columnas[iColumna] = columnas[iColumna] + 1

            if lineaVertical == 0:
                for elemento in columnas:
                    if elemento == 6:
                        clear()
                        print("   _ _                                   _   _           _ ")
                        print("  | (_)_ __   ___  __ _  __   _____ _ __| |_(_) ___ __ _| |")
                        print("  | | | '_ \ / _ \/ _` | \ \ / / _ \ '__| __| |/ __/ _` | |")
                        print("  | | | | | |  __/ (_| |  \ V /  __/ |  | |_| | (_| (_| | |")
                        print("  |_|_|_| |_|\___|\__,_|   \_/ \___|_|   \__|_|\___\__,_|_|")
                        print("=============================================================")
                        print("  de",jugadores[indiceJugador])
                        lineaVertical = lineaVertical + 1
                        time.sleep(5)
            
            if lineaHorizontal == 0:
                for elemento in filas:
                    if elemento == 5:
                        clear()
                        print("   _ _                    _                _                _        _ ")
                        print("  | (_)_ __   ___  __ _  | |__   ___  _ __(_)_______  _ __ | |_ __ _| |")
                        print("  | | | '_ \ / _ \/ _` | | '_ \ / _ \| '__| |_  / _ \| '_ \| __/ _` | |")
                        print("  | | | | | |  __/ (_| | | | | | (_) | |  | |/ / (_) | | | | || (_| | |")
                        print("  |_|_|_| |_|\___|\__,_| |_| |_|\___/|_|  |_/___\___/|_| |_|\__\__,_|_|")
                        print("=========================================================================")
                        print("  de",jugadores[indiceJugador])
                        lineaHorizontal = lineaHorizontal + 1
                        time.sleep(5)
            
            bingo = 0
            for elemento in filas:
                if elemento == 5:
                    bingo = bingo + 1

                if bingo == 6:
                    clear()
                    print("   ____ ___ _   _  ____  ___  ")
                    print("  | __ )_ _| \ | |/ ___|/ _ \ ")
                    print("  |  _ \| ||  \| | |  _| | | |")
                    print("  | |_) | || |\  | |_| | |_| |")
                    print("  |____/___|_| \_|\____|\___/ ")
                    print("================================")
                    print("  Ha ganado",jugadores[indiceJugador])
                    time.sleep(5)
                    print("")
                    esperarse = input("Puse cualquier cosa para continuar :)")
                    break
            
            if bingo == 6:
                break

            indiceJugador += 1
        
        time.sleep(2)
        
        if bingo == 6:
            break

        exit