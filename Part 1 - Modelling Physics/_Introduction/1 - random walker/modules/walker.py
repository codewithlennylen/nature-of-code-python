import random
from re import X
import pygame


RED = (255, 0, 0)


class Walker:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = RED
        self.direction: str
        self.width = 5
        self.length = 20

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
            x = self.x  # - self.width
            y = self.y - self.length

        elif self.direction == 'E':
            x = self.x + self.length
            y = self.y

        elif self.direction == 'S':
            x = self.x
            y = self.y + self.length

        elif self.direction == 'W':
            x = (self.x - self.length)  # + self.width
            y = self.y

        coordinates = (x, y)

        return coordinates

    def render(self, screen):
        if self.direction == 'N':
            x = self.x
            y = self.y - self.length
            width = self.width
            length = self.length

        elif self.direction == 'E':
            x = self.x
            y = self.y
            width = self.length
            length = self.width

        elif self.direction == 'S':
            x = self.x
            y = self.y
            width = self.width
            length = self.length

        elif self.direction == 'W':
            x = self.x - self.length
            y = self.y
            width = self.length
            length = self.width

        pygame.draw.rect(screen, self.color, (x, y,
                                              width, length))
