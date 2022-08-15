import random
import pygame


BLACK = (0, 0, 0)


class Walker:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction: str
        self.width = 15
        self.length = 60

    def step(self):
        choice: int = random.randrange(0, 4)
        if choice == 0:
            self.direction = 'N'
        elif choice == 1:
            self.direction = 'E'
        elif choice == 2:
            self.direction = 'S'
        else:
            self.direction = 'W'

    def get_new_coordinates(self):
        coordinates: tuple
        x: int
        y: int

        if self.direction == 'N':
            x = self.x
            y = self.y - self.length

        elif self.direction == 'E':
            x = self.x + self.length
            y = self.y

        elif self.direction == 'S':
            x = self.x
            y = self.y + self.length

        elif self.direction == 'W':
            x = self.x - self.length
            y = self.y

        coordinates = (x, y)

        return coordinates

    def render(self, screen):
        if self.direction == 'N':
            pygame.draw.rect(screen, BLACK, (self.x, self.y - self.length,
                                             self.width, self.length))
        elif self.direction == 'E':
            pygame.draw.rect(screen, BLACK, (self.x, self.y,
                                             self.length, self.width))
        elif self.direction == 'S':
            pygame.draw.rect(screen, BLACK, (self.x, self.y,
                                             self.width, self.length))
        elif self.direction == 'W':
            pygame.draw.rect(screen, BLACK, (self.x-self.length, self.y,
                                             self.length, self.width))
