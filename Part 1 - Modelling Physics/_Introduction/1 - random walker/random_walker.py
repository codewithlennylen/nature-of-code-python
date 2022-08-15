from modules.walker import Walker
import pygame
import sys


pygame.init()


WIDTH = 640
HEIGHT = 360
WHITE = (255, 255, 255)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 30

over = False
clock = pygame.time.Clock()

walker = Walker(WIDTH//2, HEIGHT//2)
walker.step()
# walker.render(SCREEN)
walkers = [walker]

while not over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True

    SCREEN.fill(WHITE)

    for w in walkers:
        # w.step()
        w.render(SCREEN)

    new_walker_position = walkers[-1].get_new_coordinates()
    walker = Walker(new_walker_position[0], new_walker_position[1])
    walker.step()
    # walker.render(SCREEN)
    walkers.append(walker)
    pygame.time.delay(500)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
