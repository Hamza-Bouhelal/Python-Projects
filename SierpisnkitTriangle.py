import pygame
import random


def point_on_triangle2(points):
    pt1, pt2, pt3 = points
    x, y = random.random(), random.random()
    q = abs(x - y)
    s, t, u = q, 0.5 * (x + y - q), 1 - 0.5 * (q + x + y)
    return (
        s * pt1[0] + t * pt2[0] + u * pt3[0],
        s * pt1[1] + t * pt2[1] + u * pt3[1],
    )


class SierpisnkitTriangle:
    def __init__(self, config=1):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.done = False
        if config == 1:
            self.screen = pygame.display.set_mode((1000, 1000))
            self.points = [(500, 100), (200, 900), (800, 900)]
        elif config == 2:
            self.points = [(0, 0), (0, 1000), (1800, 500)]
            self.screen = pygame.display.set_mode((1800, 1000))
        elif config == 3:
            self.points = [(random.randint(0, 1000), random.randint(0, 1000))
                           for i in range(3)]
            self.screen = pygame.display.set_mode((1000, 1000))
        self.screen.fill((255, 255, 255))
        self.color = (0, 0, 0)
        self.linewidth = 3
        self.pointWidth = 1
        pygame.draw.lines(self.screen, self.color,
                          True, self.points, self.linewidth)
        self.inPoints = [point_on_triangle2(self.points)]

    def draw(self):
        self.drawNewPoint()
        pygame.draw.circle(self.screen, self.color,
                           self.inPoints[-1], self.pointWidth)

    def drawNewPoint(self):
        i = random.randint(0, 2)
        self.inPoints.append(
            ((self.inPoints[-1][0] + self.points[i][0]) / 2, (self.inPoints[-1][1] + self.points[i][1]) / 2))

    def run(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
            self.draw()
            pygame.display.flip()


if __name__ == "__main__":
    app = SierpisnkitTriangle(3)
    app.run()
    pygame.quit()
