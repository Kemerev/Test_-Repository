import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('ТЕКСТ') 

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (169, 169, 169)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(WHITE)

    pygame.draw.rect(window, RED, (300, 200, 200, 200))
   
    pygame.draw.polygon(window, BLUE, [(300, 200), (500, 200), (400, 100)])
    
    pygame.draw.rect(window, BLUE, (370, 300, 60, 100))

    pygame.display.update()

pygame.quit()
sys.exit()