import pygame
import sys
import random
import math

Ancho_Ventana = 800
Largo_Ventana = 480


Negro = (0, 0, 0)
Gris = (120, 120, 120)
Blanco = (255, 255, 255)


Velocidad_jugador = 5
Velocidad_compu = 4


x_balon = 0
y_balon = 0
radio = 10
Velocidad_balon = 3
direccion_x_balon = 1
direccion_y_balon = 1

x_jugador = 30
y_jugador= Largo_Ventana // 2
ancho_jugador = 20
largo_jugador = 100
marcador_jugador = 0

x_compu = Ancho_Ventana - 60
y_compu = Largo_Ventana // 2
ancho_compu = 20
largo_compu = 100
marcador_compu = 0

prediccion_y = 0

def cambio_direccion_x():
    global direccion_x_balon
    direccion_x_balon *= -1

def cambio_direccion_y():
    global direccion_y_balon
    direccion_y_balon *= -1

def lanzamiento():
    global direccion_x_balon
    global x_balon
    global y_balon
    global Velocidad_balon
    x_balon = Ancho_Ventana // 2
    y_balon = Largo_Ventana // 2
    direccion_x_balon = 1 if random.randint(0,1) % 2 else -1
    Velocidad_balon = 3

def movimiento_balon():
    global x_balon
    global y_balon
    x_balon += direccion_x_balon * Velocidad_balon
    y_balon += direccion_y_balon * Velocidad_balon

def rebote():
    global direccion_y_balon
    if y_balon - radio < 0 or y_balon + radio > Largo_Ventana:
        direccion_y_balon *= -1

def fuera():
    return x_balon + radio < 0 or x_balon - radio > Ancho_Ventana


def rebote_balon(x, y, ancho, largo):
    lado_izquierdo, superposicion_izquierda = fisicas(x, y, largo)
    if lado_izquierdo:
        return lado_izquierdo, superposicion_izquierda
    
    lado_derecho, superposicion_derecha = fisicas(x + ancho, y, largo)
    return lado_derecho, superposicion_derecha

def fisicas(x, y, largo):
    a = 1
    b = -2 * y_balon
    c = y_balon**2 + x**2 - 2 * x * x_balon + x_balon**2 - radio**2
    discriminante = b**2 - 4 * a * c
    if discriminante < 0:
        return (False, False)
    elif discriminante == 1:
        y = (-b + (math.sqrt(discriminante))) / (2 * a)
        return (True, y < y < y + largo)
    else:
        y0 = (-b + (math.sqrt(discriminante))) / (2 * a)
        y1 = (-b - (math.sqrt(discriminante))) / (2 * a)
        return (True, y < y0 < y + largo or y < y1 < y + largo)
        

def prediccion_compu():
    prediccion_dir = direccion_y_balon
    y = y_balon
    for x in range(x_balon + radio, x_compu, Velocidad_balon):
        if y - radio < 0 or y + radio > Largo_Ventana:
            prediccion_dir *= -1
        y += Velocidad_balon * prediccion_dir
    return y

def ia():
    global prediccion_y
    global y_compu
    if direccion_x_balon == 1 and x_balon > Ancho_Ventana // 2:
        prediccion_y = prediccion_compu()
        if prediccion_y > 0 and prediccion_y < Largo_Ventana and (prediccion_y < y_compu or prediccion_y > y_compu + largo_compu):
            y_compu += Velocidad_compu * (-1 if prediccion_y < y_compu else 1)

def texto1(texto, x, y):
    fuente = pygame.font.Font("./LLPIXEL3.ttf", 20)
    tipo = fuente.render(texto, False, Blanco)
    fondo.blit(tipo, (x, y))    
    
def texto2(texto, x, y):
    fuente = pygame.font.Font("./LLPIXEL3.ttf", 50)
    tipo = fuente.render(texto, False, Blanco)
    fondo.blit(tipo, (x, y)) 


pygame.init()
fondo = pygame.display.set_mode((Ancho_Ventana, Largo_Ventana))
pygame.display.set_caption('Pong Game Arcade')
pygame.font.init()
lanzamiento()
ronda_ganada = False
tick = 0
juego_terminado = False

while True:
    pygame.time.delay(5)
    fondo.fill(Negro)
    movimiento_balon()
    rebote()
    
    if juego_terminado==False:
        if ronda_ganada and fuera():
            ronda_ganada = False
            lanzamiento()
            pygame.time.delay(500)
            continue
        
        linea_jugador_alcanzada, jugador_defendido = rebote_balon(x_jugador, y_jugador, ancho_jugador, largo_jugador)
        
        if linea_jugador_alcanzada:       
            if not ronda_ganada and jugador_defendido:
                cambio_direccion_x()
            elif not ronda_ganada and not jugador_defendido:
                ronda_ganada = True
                marcador_compu += 1
            elif ronda_ganada and jugador_defendido:
                cambio_direccion_y()
        
        linea_compu_alcanzada, compu_defendio = rebote_balon(x_compu, y_compu, ancho_compu, largo_compu)
        if linea_compu_alcanzada:
            if not ronda_ganada and compu_defendio:
                cambio_direccion_x()
            elif not ronda_ganada and not compu_defendio:
                ronda_ganada = True
                marcador_jugador +=1
            elif ronda_ganada and compu_defendio:
                cambio_direccion_y()
                
        ia()
        
        tick += 1
        if tick % 500 == 0:
            Velocidad_balon += 1


    texto1('Player', (Ancho_Ventana/2)-100, 10)
    texto2(str(marcador_jugador), (Ancho_Ventana/2)-70, 45)
    texto1('Computer', (Ancho_Ventana/2)+50, 10)
    texto2(str(marcador_compu), (Ancho_Ventana/2)+50, 45)
    pygame.draw.rect(fondo, Blanco, (x_jugador, y_jugador, ancho_jugador, largo_jugador), 0)
    pygame.draw.rect(fondo, Blanco, (x_compu, y_compu, ancho_compu, largo_compu), 0)
    pygame.draw.circle(fondo, Blanco, (x_balon, y_balon), radio)
    
    
    for i in range(1, Largo_Ventana // 10):
        if i % 2 == 0:
            pygame.draw.rect(fondo, Gris, (Ancho_Ventana // 2, i * 10, 10, 10), 0)
            
            
    if marcador_jugador >= 12:
        juego_terminado=True
        texto2('You Win!!!!', (Ancho_Ventana/3),(Largo_Ventana/3))
        texto1('Presiona "Esc" para salir', (Ancho_Ventana/3)+20,(Largo_Ventana*2/3))
    if marcador_compu >= 12:
        juego_terminado=True
        texto2('You Lose!!!!', (Ancho_Ventana/3),(Largo_Ventana/3))
        texto1('Presiona "Esc" para salir', (Ancho_Ventana/3)+20,(Largo_Ventana*2/3))

            
    pygame.display.update()
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_UP]:
        linea_alcanzada, superposicion = rebote_balon(x_jugador, y_jugador, ancho_jugador, largo_jugador)
        if linea_alcanzada and y_jugador - Velocidad_jugador < y_balon + radio:
            continue
        y_jugador = 0 if y_jugador - Velocidad_jugador < 0 else y_jugador - Velocidad_jugador 

        
    if teclas[pygame.K_DOWN]:
        linea_alcanzada, superposicion = rebote_balon(x_jugador, y_jugador, ancho_jugador, largo_jugador)
        if linea_alcanzada and y_jugador + largo_jugador + Velocidad_jugador > y_balon - radio:
            continue
        y_jugador = Largo_Ventana - largo_jugador if y_jugador + largo_jugador + Velocidad_jugador > Largo_Ventana else y_jugador + Velocidad_jugador

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
