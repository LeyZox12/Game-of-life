import pygame
from math import sin,cos,pi
from time import sleep
pygame.init()
screen = pygame.display.set_mode((512,512))
pygame.display.set_caption("Conway's Game of Life")
ouvert = True
tailleGrille = int(input("Taille de la grille:"))
grille = [[False for _ in range(tailleGrille)] for _ in range(tailleGrille)]
ratio = 512/tailleGrille
color = 50
estEnPause = True
fps = 10
xpos,ypos = 0,0
appuiSouris = False
def updateCells():
    buffer = [[False for _ in range(tailleGrille)] for _ in range(tailleGrille)]
    
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            voisins = 0
            if grille[(i-1)%tailleGrille][(j+1)%tailleGrille]:
                voisins+=1
            if grille[(i-1)%tailleGrille][j]:
                voisins+=1
            if grille[(i-1)%tailleGrille][(j-1)%tailleGrille]:
                voisins+=1
            if grille[i][(j+1)%tailleGrille]:
                voisins+=1
            if grille[i][(j-1)%tailleGrille]:
                voisins+=1
            if grille[(i+1)%tailleGrille][(j+1)%tailleGrille]:
                voisins+=1
            if grille[(i+1)%tailleGrille][j]:
                voisins+=1
            if grille[(i+1)%tailleGrille][(j-1)%tailleGrille]:
                voisins+=1
            if voisins == 3 or voisins == 2 and grille[i][j]:
                buffer[i][j] = True
            else:
                buffer[i][j] = False
    return buffer
while ouvert:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            ouvert = False
        if e.type == pygame.MOUSEMOTION:
            xpos,ypos = e.pos
            xpos //= ratio
            ypos //= ratio
        if e.type == pygame.MOUSEBUTTONDOWN:
            appuiSouris = True
            isDrawing = e.button == 1
        if e.type == pygame.MOUSEBUTTONUP:
            appuiSouris = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            estEnPause = not estEnPause
            
    screen.fill((0,0,0))
    if appuiSouris:
        grille[int(ypos)][int(xpos)] = isDrawing
    if not estEnPause:
        grille = updateCells()
        sleep(1/fps)
    
    y=0
    for i in grille:
        x=0
        for j in i:
            if j:
                pygame.draw.rect(screen, (255,255,255),(x*ratio,y*ratio,ratio,ratio))
            x+=1
        y+=1
    for i in range(tailleGrille):
        pygame.draw.line(screen,(color,color,color),(0,ratio*i),(512,ratio*i))
        pygame.draw.line(screen,(color,color,color),(ratio*i,0),(ratio*i,512))
    pygame.display.flip()