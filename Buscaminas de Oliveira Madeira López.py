def tablero(cant):
    letras=[" 0", " 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9"]
    numeros=["0","1","2","3","4","5","6","7","8","9",]
    matriz=[]
    listacentral=[]
    
    for i in range (cant):
        listacentral.append("⬜")
    
    for i in range (cant):
        matriz.append(listacentral.copy())  # funcion generadora del tablero limpio
    
    print(' ',' '.join(letras[0:cant]))

    for i in range (cant):
        print(numeros[i],' '.join(matriz[i]))
    return matriz    

    
def elementos_matriz(cant):
    listacentral=[]
    
    for i in range (cant*cant):
        listacentral.append("⬜")  # funcion generadora del tablero sucio

    return listacentral

import random

def bombas(total_bombas,cant):
    elementos=elementos_matriz(cant)
    matriz = []
    i=0
    while i<total_bombas:
        casilla=random.randint(0,cant*cant-1)    # esto pone las bombas dentro de la lista de elementos de la matriz y la convierte en matriz nuevamente
        if elementos[casilla]!="💣":
            elementos[casilla]="💣"
            i+=1
    
    for i in range(0, cant):
        matriz.append(elementos[cant * i: cant * (i + 1)])
    
    return matriz


def examinar_casilla(fila,columna,matriz):
    casilla=matriz[fila][columna]       # funcion que determina si hay bomba o no
    if casilla!="💣":
        return False
    if casilla=="💣":
        return True
    
    

def nohaybomba(fila,columna,matriz,cant):  # genera los números del tablero segun cantidad de bomas alrededor
    contador_bombas=0

    if examinar_casilla(x,y,tablerosucio)==(True):
        
        cadena="fin del juego"
        return cadena
    else:
        if fila==0 and columna==cant-1: # esquina derecha arriba
            if matriz[fila][columna-1]=="💣":
                contador_bombas+=1
            if matriz[fila+1][columna]=="💣":  
                contador_bombas+=1
            if matriz[fila+1][columna-1]=="💣":  
                contador_bombas+=1              # esquinas
        elif columna==0 and fila==cant-1:            # esquina izquierda baja
            if matriz[fila-1][columna]=="💣":
                contador_bombas+=1
            if matriz[fila][columna+1]=="💣":
                contador_bombas+=1
            if matriz[fila-1][columna+1]=="💣":  
                    contador_bombas+=1
        elif fila==cant-1 and columna==cant-1:    # esquina baja derecha
            if matriz[fila-1][columna]=="💣":
                contador_bombas+=1
            if matriz[fila][columna-1]=="💣":
                contador_bombas+=1
            if matriz[fila-1][columna-1]=="💣":  
                contador_bombas+=1
        elif fila==0 and columna==0:          # esquina alta izquierda
            if matriz[fila+1][columna]=="💣":
                contador_bombas+=1
            if matriz[fila][columna+1]=="💣":
                contador_bombas+=1
            if matriz[fila+1][columna+1]=="💣":  
                contador_bombas+=1
        elif columna==0 and (fila>0 and fila<cant-1):
            if matriz[fila+1][columna]=="💣":
                contador_bombas+=1
            if matriz[fila][columna+1]=="💣":
                contador_bombas+=1                  #lado izquierdo
            if matriz[fila-1][columna]=="💣":
                contador_bombas+=1
            if matriz[fila+1][columna+1]=="💣":
                contador_bombas+=1
            if matriz[fila-1][columna+1]=="💣":
                contador_bombas+=1
        elif columna==cant-1 and (fila>0 and fila<cant-1):
            if matriz[fila+1][columna]=="💣":
                contador_bombas+=1
            if matriz[fila][columna-1]=="💣":
                contador_bombas+=1                  #lado derecho
            if matriz[fila-1][columna]=="💣":
                contador_bombas+=1
            if matriz[fila+1][columna-1]=="💣":
                contador_bombas+=1
            if matriz[fila-1][columna-1]=="💣":
                contador_bombas+=1
        elif fila==0 and (columna>0 and columna<cant-1):
            if matriz[fila+1][columna]=="💣":
                contador_bombas+=1
            if matriz[fila][columna+1]=="💣":
                contador_bombas+=1                  # lado de arriba
            if matriz[fila][columna-1]=="💣":
                contador_bombas+=1
            if matriz[fila+1][columna+1]=="💣":
                contador_bombas+=1
            if matriz[fila+1][columna-1]=="💣":
                contador_bombas+=1
        elif fila==cant-1 and (columna>0 and columna<cant-1):
            if matriz[fila-1][columna]=="💣":
                contador_bombas+=1
            if matriz[fila][columna+1]=="💣":
                contador_bombas+=1                  # lado de abajo
            if matriz[fila][columna-1]=="💣":
                contador_bombas+=1
            if matriz[fila-1][columna+1]=="💣":
                contador_bombas+=1
            if matriz[fila-1][columna-1]=="💣":
                contador_bombas+=1
        else:
            if matriz[fila-1][columna]=="💣":  # casillas comunes
                contador_bombas+=1
            if matriz[fila+1][columna]=="💣":
                contador_bombas+=1
            if matriz[fila][columna-1]=="💣":
                contador_bombas+=1
            if matriz[fila][columna+1]=="💣":
                contador_bombas+=1
            if matriz[fila-1][columna-1]=="💣":
                contador_bombas+=1
            if matriz[fila-1][columna+1]=="💣":
                contador_bombas+=1
            if matriz[fila+1][columna-1]=="💣":
                contador_bombas+=1
            if matriz[fila+1][columna+1]=="💣":
                contador_bombas+=1
        matriz[fila][columna]=' '+str(contador_bombas)
    
    return contador_bombas

def imprimir_tablero(cant,tablero,fila,columna):
    letras=[" 0", " 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9"]
    numeros=["0","1","2","3","4","5","6","7","8","9",]
    
    tablero[fila][columna]=' '+str(nohaybomba(x,y,tablerosucio,cantidad))  #reemplaza la coordenada del usuario por el numero de bombas
    
    print(' ',' '.join(letras[0:cant]))
  
    for i in range (cant):
        print(numeros[i],' '.join(tablero[i]))
    
    return tablero

opcionusuario=1
while opcionusuario==1:

    print('\n★━━━━━━❀ Bienvenid@ al BUSCAMINAS ❀━━━━━━★')
    cantidad=int(input("\nIngrese dimensiones deseadas para el tablero en formato numérico (3-10): \nej: si desea un tablero de 3x3 ingrese 3: "))

    while cantidad<3 or cantidad>10:
        cantidad=int(input("vuelva a ingresar dimensiones válidas para el tablero: \n(no menores a 3 ni mayor que 10): "))

    casillastotales=cantidad**2
    diez_porc_casillas=int(casillastotales*0.1)
    quince_porc_casillas=int(casillastotales*0.15)
    veinte_porc_casillas=int(casillastotales*0.20)
    veinticinco_porc_casillas=int(casillastotales*0.25)

    cantidad_bombas=int(input(f"\ningrese cantidad de bombas: \n(procure que esta no sea 0 ni mayor o igual a la cantidad de casillas de su tablero) \n Fácil: entre {diez_porc_casillas} y {quince_porc_casillas}. \n Medio: entre {quince_porc_casillas} y {veinte_porc_casillas}. \n Difícil: entre {veinte_porc_casillas} y {veinticinco_porc_casillas}. \n Bombas: "))

    while cantidad_bombas <=0 or cantidad_bombas>=casillastotales:
        cantidad_bombas=int(input("vuelva a ingresar un número válido de cantidad de bombas: \n(procure que esta no sea 0 ni igual a la cantidad de casillas de su tablero) "))
            
    tablero_matriz = tablero(cantidad)

    tablerosucio=bombas(cantidad_bombas,cantidad) 

    print("\n ingrese las coordenadas de la casilla que desea descubrir")
    y=(int(input("x: ")))                                # comienza el juego, eleccion de casilla
    x=(int(input("y: ")))
    numero_de_jugadas=1
    casillas_sin_bombas=casillastotales-cantidad_bombas

    while examinar_casilla(x,y,tablerosucio)==(False) and numero_de_jugadas!=casillas_sin_bombas:
        imprimir_tablero(cantidad,tablero_matriz,x,y)
        print("\n ingrese las coordenadas de la casilla que desea descubrir")
        y=(int(input("x: ")))                               
        x=(int(input("y: ")))
        numero_de_jugadas+=1

    if numero_de_jugadas==casillas_sin_bombas and examinar_casilla(x,y,tablerosucio)==(False):
        print('\n¡Has ganado!')
    elif examinar_casilla(x,y,tablerosucio)==(True):
        print("\n¡¡¡BOOM!!! \nTu casilla contenia una bomba :(\n")
        for i in range (cantidad):
            print(' '.join(tablerosucio[i]))   

    print("\n1. Volver a jugar")
    print("2. Salir")
    opcionusuario=int(input("ingrese una opción: \n"))

print('\n ----╚✩╡¡Gracias por jugar!╞✩╝----\n')  