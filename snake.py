import pygame, sys, time, random
from pygame.locals import *

pygame.init()
play_surface = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()

def comida_generador():
    comida_pos = [random.randint(0,49)*10, random.randint(0,49)*10]
    return comida_pos
def main():
    snake_pos = [100,50]
    snake_cuerpo = [[100,50], [90,50],[50,80]]
    direccion = "RIGHT"
    cambio = direccion
    comida_pos = comida_generador()
    score = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        cambio = "RIGHT"
                    if event.key == pygame.K_LEFT:
                        cambio = "LEFT"
                    if event.key == pygame.K_UP:
                        cambio = "UP"
                    if event.key == pygame.K_DOWN:
                        cambio = "DOWN"

        if cambio == "RIGHT" and direccion != "LEFT":
            direccion = "RIGHT"
        if cambio == "LEFT" and direccion != "RIGHT":
            direccion = "LEFT"
        if cambio == "UP" and direccion != "DOWN":
            direccion = "UP"
        if cambio == "DOWN" and direccion != "UP":
            direccion = "DOWN"

        if direccion == "RIGHT":
            snake_pos[0] += 10
        if direccion == "LEFT":
            snake_pos[0] -= 10
        if direccion == "UP":
            snake_pos[1] -= 10
        if direccion == "DOWN":
            snake_pos[1] += 10

        snake_cuerpo.insert(0, list(snake_pos))
        if snake_pos == comida_pos:
            comida_pos = comida_generador()
            score += 1
        else:
            snake_cuerpo.pop()

        play_surface.fill((0,0,0))

        for pos in snake_cuerpo:
            pygame.draw.rect(play_surface, (200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(play_surface, (255,160,60), pygame.Rect(comida_pos[0], comida_pos[1], 10, 10))


        if snake_pos[0] >= 500 or snake_pos[0] <=0:
            print(f"GAME OVER!")
            print(f"Marcador final: {score}")
            run = False
        if snake_pos[1] >= 500 or snake_pos[1] <=0:
            print(f"GAME OVER!")
            print(f"Marcador final: {score}")
            run = False

        if snake_pos in snake_cuerpo[1:]:
            print(f"GAME OVER!")
            print(f"Marcador final: {score}")
            run = False

        pygame.display.flip()
        fps.tick(10)

main()
pygame.quit()

