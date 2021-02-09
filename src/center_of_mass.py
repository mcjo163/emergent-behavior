# center_of_mass.py
# In this simulation, points travel toward the center of 
# mass of the system.

import pygame as pg
from random import randint


SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


class Point:
    def __init__(self, x, y, modifier):
        self.pos = pg.Vector2(x, y)
        self.modifier = modifier

        self.vel = pg.Vector2(0, 0)
    
    def update_trajectory(self, com):
        """updates this point's trajectory based on given center of mass"""
        self.vel += (com - self.pos) / self.modifier
    
    def draw(self, surf):
        pg.draw.circle(surf, WHITE, self.pos, 2)

    def draw_velocity(self, surf):
        pg.draw.line(surf, BLUE, self.pos, self.pos+self.vel)


def get_com(points):
    com = pg.Vector2(0, 0)
    for point in points:
        com += point.pos
    com /= len(points)
    return com


def main():

    # initialize and set up pygame
    pg.init()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Center of Mass Emergent Behavior")

    clock = pg.time.Clock()

    # generate 100 random points
    points = []
    for _ in range(100):
        points.append(Point(
            randint(0, SCREEN_WIDTH), 
            randint(0, SCREEN_HEIGHT),
            randint(200, 500)))
    
    com = get_com(points)
    
    for point in points:
        point.update_trajectory(com)
        point.vel = pg.Vector2(point.vel.y, -point.vel.x) * 8


    # main loop
    done = False
    while not done:

        # event handling
        for event in pg.event.get():

            # handle window close event
            if event.type == pg.QUIT:
                done = True
        
        # frame processing
        com = get_com(points)

        for point in points:
            point.update_trajectory(com)
            point.pos += point.vel

        # display handling
        screen.fill(BLACK)

        for point in points:
            point.draw_velocity(screen)
            point.draw(screen)

        pg.draw.circle(screen, BLUE, com, 5)
        
        pg.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
