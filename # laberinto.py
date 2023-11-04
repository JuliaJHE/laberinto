# laberinto
# Pedir el nombre del jugador por teclado
nombre_jugador = input("Ingrese su nombre: ")

# Definir el laberinto como una lista de cadenas
laberinto = [
    "#######################",
    "#P....................#",
    "#.###################.#",
    "#.#.................#.#",
    "#.#.###############...#",
    "#.#.#...............#.#",
    "#.#.#.###############.#",
    "#.#.#.#...............#",
    "#.#.#.#..##############",
    "#.#.#.................#",
    "#.#.#################.#",
    "#.#...................#",
    "#.#.###################",
    "#.....................#",
    "#######################"
]

# Función para imprimir el laberinto en la pantalla
def imprimir_laberinto():
    for fila in laberinto:
        print(fila)

# Función para mover al personaje en el laberinto
def mover_personaje(direccion):
    global laberinto
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == 'P':
                if direccion == 'w' and laberinto[i - 1][j] == '.':
                    # Mover hacia arriba
                    laberinto[i - 1] = laberinto[i - 1][:j] + 'P' + laberinto[i - 1][j + 1:]
                    laberinto[i] = laberinto[i][:j] + '.' + laberinto[i][j + 1:]
                elif direccion == 's' and laberinto[i + 1][j] == '.':
                    # Mover hacia abajo
                    laberinto[i + 1] = laberinto[i + 1][:j] + 'P' + laberinto[i + 1][j + 1:]
                    laberinto[i] = laberinto[i][:j] + '.' + laberinto[i][j + 1:]
                elif direccion == 'a' and laberinto[i][j - 1] == '.':
                    # Mover hacia la izquierda
                    laberinto[i] = laberinto[i][:j - 1] + 'P' + laberinto[i][j] + laberinto[i][j + 1:]
                elif direccion == 'd' and laberinto[i][j + 1] == '.':
                    # Mover hacia la derecha
                    laberinto[i] = laberinto[i][:j] + laberinto[i][j + 1] + 'P' + laberinto[i][j + 2:]

# Mensaje de bienvenida con el nombre del jugador
print(f"Bienvenido, {nombre_jugador}! Comienza a explorar el laberinto.")

# Bucle principal del juego
while True:
    imprimir_laberinto()
    movimiento = input("Mueve al personaje (↑w ↓s ←a →d o Q para salir): ")
    if movimiento == 'Q':
        break
    if movimiento in ['w', 's', 'a', 'd']:
        mover_personaje(movimiento)
    else:
        print("Movimiento no válido. Usa w s a d o Q para salir.")
