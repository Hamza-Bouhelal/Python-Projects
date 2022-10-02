import pygame
from random import shuffle, randrange
import time


def make_maze(w, h):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "+  "
            if yy == y:
                ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s


class movingRectangle:
    def __init__(self, color):
        self.x = 15
        self.y = 40
        self.width = 10
        self.height = 10
        self.color = color
        self.velocity = 2
        self.direction = []
        self.bullets = []
        self.shootCooldown = 0
        self.bulletVelocity = 10
        self.windowWidth = 1500
        self.windowheight = 800
        self.rect = None
        self.wallswidth = 30
        self.maxShootCooldown = 60
        self.round = 0
        self.exits = 3
        self.eyerange = 120
        self.seeAll = False
        self.maxseealltime = 180
        self.seeAllBar = int(self.maxseealltime)
        self.changesightcooldown = 30
        self.wins = 0
        self.wonthisround = False
        self.generateNewmaze(self.exits)
        self.mainLoop()

    def generateNewmaze(self, exits):
        self.currentMaze = make_maze(
            self.windowWidth//100,  5 + self.windowheight//100)
        splitted = self.currentMaze.split("\n")
        mazewitexits = splitted[0] + "\n"
        justchose = 3
        self.exitsindexs = []
        for i in range(1, len(splitted)):
            if i == 1:
                mazewitexits += " " + splitted[i][1:] + "\n"
            else:
                if exits > 0 and splitted[i][len(splitted[0]) - 2] == ' ' and justchose == 0:
                    mazewitexits += splitted[i][: len(splitted[0]) - 2] + " \n"
                    exits -= 1
                    self.exitsindexs.append(i)
                    justchose = 8
                else:
                    mazewitexits += splitted[i] + "\n"
            if justchose > 0:
                justchose -= 1
        if self.exits != 1:
            self.exits -= 1
        self.currentMaze = mazewitexits
        self.x = 15
        self.y = 40
        if self.velocity != 5:
            self.velocity += 1
        self.direction = []
        self.bullets = []
        self.shootCooldown = 0
        self.round += 1
        self.changesightcooldown = 60
        if self.maxShootCooldown > 10:
            self.maxShootCooldown -= 5
        if self.eyerange > 50:
            self.eyerange -= 9
        self.seeAll = False
        self.maxseealltime += 20 if self.maxseealltime < 500 else 0
        self.seeAllBar = int(self.maxseealltime)
        self.wonthisround = False

    def draw(self, surface):
        self.finishLine = pygame.draw.rect(surface, (255, 215, 0),
                                           (self.wallswidth * (len(self.currentMaze.split("\n")[0])), 0, self.windowWidth, self.windowheight))
        self.scoreboard = pygame.draw.rect(surface, (255, 255, 255),
                                           (0, self.windowheight, self.windowWidth, 150))
        t = self.windowWidth - 120
        ttt = [(self.exitsindexs[i]-1) *
               self.wallswidth + 7 for i in range(len(self.exitsindexs))]
        for tt in ttt:
            pygame.draw.polygon(surface, (255, 0, 0), ((
                0+t, 25+tt), (0+t, tt+50), (50+t, tt+50), (50+t, 75+tt), (75+t, 37+tt), (50+t, 0+tt), (50+t, 25+tt)))
        eyebar = pygame.font.SysFont(
            None, 40).render(
            f"Sight cooldown:", 1, (0, 0, 0))
        surface.blit(eyebar, (3*self.windowWidth/4 - eyebar.get_width() /
                     2 - 30, self.windowheight + 50 - eyebar.get_height()/2))
        pygame.draw.rect(surface, (0, 0, 0),
                         (self.windowWidth - 250, self.windowheight + 35, 200, 30))
        pygame.draw.rect(surface, (255, 255, 255),
                         (self.windowWidth - 250 + 3, self.windowheight + 35 + 3, 194, 24))
        # draw eye range bar
        percentage = self.seeAllBar / self.maxseealltime
        color = (255, 0, 0) if percentage < 0.33 else (
            (0, 255, 0) if percentage > 0.66 else (255, 165, 0))
        pygame.draw.rect(surface, color,
                         ((self.windowWidth - 250 + 6), self.windowheight + 35 + 6, 188 * percentage, 18))
        largeFont = pygame.font.SysFont(
            None, 40)
        round = largeFont.render(
            f"Round: {self.round}, (w: {self.wins})", 1, (0, 0, 0))
        surface.blit(round, (self.windowWidth/2 - round.get_width() /
                     2 - 240, self.windowheight + 50 - round.get_height()/2))
        largeFont = pygame.font.SysFont(
            None, 30)
        control = largeFont.render(
            "Move: Arrows" + " " * 30 + "New Maze: m" + " " * 30 + "Shoot: space" + " " * 30 + "View Full Maze: a" + " " * 30 + "Reset Position: r", 1, (0, 0, 0))
        surface.blit(control, (20, self.windowheight +
                     120 - control.get_height()/2))
        reloadfq = pygame.font.SysFont(
            None, 40).render(
            f"Reload Fq: {self.maxShootCooldown/60:.1f} secs", 1, (0, 0, 0))
        surface.blit(reloadfq, (self.windowWidth/4 - reloadfq.get_width() /
                     2 - 200, self.windowheight + 50 - reloadfq.get_height()/2))
        velocity = pygame.font.SysFont(
            None, 40).render(
            f"Velocity: {self.velocity}", 1, (0, 0, 0))
        surface.blit(velocity, (3*self.windowWidth/4 - velocity.get_width() /
                     2 - 330, self.windowheight + 50 - velocity.get_height()/2))
        self.rect = pygame.draw.rect(surface, self.color,
                                     (self.x, self.y, self.width, self.height))
        toremove = []

        for i in range(len(self.bullets)):
            bullet = self.bullets[i]
            prevpos = bullet[0]
            direction = bullet[1]
            pos = [prevpos[j] + direction[j] for j in range(2)]
            self.bullets[i][2] = pygame.draw.circle(surface, self.color,
                                                    (pos[0], pos[1]), 5)
            self.bullets[i][0] = pos
            if pos[0] > self.windowWidth or pos[0] < 0 or pos[1] > self.windowheight or pos[1] < 0:
                toremove.append(i)
            bordertoremove = []
            tempx, tempy = pos[0] + (self.width/2 if direction[0] > 0 else -self.width/2), pos[1] + (
                self.width/2 if direction[1] > 0 else -self.width/2)
            for j in range(len(self.borders)):
                if self.borders[j].collidepoint(tempx, tempy):
                    toremove.append(i)
                    tempi, tempj = self.iandjfromxandy(tempx, tempy)
                    self.removeborder(tempi, tempj)

        for i in toremove:
            self.bullets.pop(i)

    def removeborder(self, tempi, tempj):
        splitted = self.currentMaze.split("\n")
        if splitted[tempi][tempj] != " ":
            stri = ""
            for k in range(len(splitted)):
                for l in range(len(splitted[k])):
                    if k == tempi and l == tempj:
                        stri += " "
                    else:
                        stri += splitted[k][l]
                stri += "\n"
            self.currentMaze = stri

    def iandjfromxandy(self, x, y):
        return int(y/self.wallswidth), int(x/self.wallswidth)

    def drawMaze(self, surface):
        borders = []
        splitted = self.currentMaze.split('\n')
        w = self.wallswidth

        for i in range(len(splitted)):
            for j in range(len(splitted[i])):
                if splitted[i][j] != ' ':
                    borders.append(pygame.draw.rect(surface, (144, 234, 144),
                                                    (w * j, w * i, w, w)))
        self.borders = borders

    def draweyecover(self, screen):
        if not self.seeAll:
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.x - 1000, self.y + self.eyerange, 2000, 2000))
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.x + self.eyerange, self.y - 1000, 2000, 2000))
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.x-1000, self.y - self.eyerange-2000, 2000, 2000))
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.x - self.eyerange-2000, self.y-1000, 2000, 2000))

    def move(self, surface):
        direction = [0, 0]
        prevX, prevY = self.x, self.y
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.x - self.velocity > 0:
            self.x -= self.velocity
            direction[0] = -self.bulletVelocity
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and self.x + self.width + self.velocity < self.windowWidth:
            self.x += self.velocity
            direction[0] = self.bulletVelocity
        if pygame.key.get_pressed()[pygame.K_UP] and self.y - self.velocity > 0:
            self.y -= self.velocity
            direction[1] = -self.bulletVelocity
        elif pygame.key.get_pressed()[pygame.K_DOWN] and self.y + self.height + self.velocity < self.windowheight:
            self.y += self.velocity
            direction[1] = self.bulletVelocity
        x, y = self.x + direction[0] - (self.width/2 if direction[0] > 0 else -self.width /
                                        2), self.y + direction[1] - (self.width/2 if direction[1] > 0 else -self.width/2)

        """ temprect = pygame.draw.rect(surface, self.color,
                                    (self.x + direction[0], self.y + direction[1], self.width, self.height))
        if self.scoreboard.colliderect(temprect) or any([border.colliderect(temprect) for border in self.borders if not border.collidepoint(self.x, self.y)]):
            self.x = prevX
            self.y = prevY """
        if self.scoreboard.collidepoint(x, y) or any([border.collidepoint(x, y) for border in self.borders if not border.collidepoint(self.x, self.y)]):
            self.x = prevX
            self.y = prevY
        elif direction != [0, 0]:
            self.direction = direction
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if self.shootCooldown == 0:
                direction = self.direction if self.direction != [] else [0, 0]
                newx, newy = self.x + \
                    direction[0] + self.width / 2, self.y + \
                    direction[1] + self.width / 2
                self.bullets.append(
                    [[newx, newy], direction, pygame.draw.circle(surface, self.color,
                                                                 (newx, newy), self.width/2)])
                self.shootCooldown = int(self.maxShootCooldown)
                for i in range(len(self.bullets)):
                    if self.bullets[i][1] == [0, 0]:
                        self.bullets.pop(i)
        if pygame.key.get_pressed()[pygame.K_a] and self.changesightcooldown == 60:
            if self.seeAll:
                self.seeAll = False
                self.changesightcooldown = 0
            else:
                if self.seeAllBar > self.maxseealltime / 4:
                    self.seeAll = True
                    self.changesightcooldown = 0
        if pygame.key.get_pressed()[pygame.K_r]:
            self.x, self.y = 15, 40
        if pygame.key.get_pressed()[pygame.K_m]:
            self.generateNewmaze(self.exits)
            time.sleep(1)
        else:
            if self.shootCooldown > 0:
                self.shootCooldown -= 1

    def checksightsetting(self):
        if self.changesightcooldown != 60:
            self.changesightcooldown += 1
        if self.seeAll:
            if self.seeAllBar - 2 > 0:
                self.seeAllBar -= 2
            else:
                self.seeAll = False
        else:
            if self.seeAllBar != int(self.maxseealltime):
                self.seeAllBar += 1

    def mainLoop(self):
        pygame.init()
        screen = pygame.display.set_mode(
            (self.windowWidth, self.windowheight + 150))
        pygame.display.set_caption("Maze Generator Game")
        clock = pygame.time.Clock()
        winmsgappeared = 180
        while True:
            if winmsgappeared == 0:
                winmsgappeared = 180
                self.generateNewmaze(self.exits)
                time.sleep(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.fill((0, 0, 0))
            self.checksightsetting()
            self.drawMaze(screen)
            self.draweyecover(screen)
            self.draw(screen)
            self.move(screen)
            if self.finishLine.collidepoint(self.x + self.width/2, self.y + self.height/2) and not self.wonthisround:
                self.wonthisround = True
                self.wins += 1
                self.seeAllBar = int(self.maxseealltime)
                self.seeAll = True
            if self.wonthisround:
                winmsgappeared -= 1
                largeFont = pygame.font.SysFont(
                    None, 82)
                winmsg = largeFont.render(
                    "YOU WIN THIS ROUND", 1, self.color)
                screen.blit(winmsg, (self.windowWidth/2 - winmsg.get_width() /
                            2, self.windowheight/2 - winmsg.get_height()/2))
                largeFont = pygame.font.SysFont(
                    None, 80)
                winmsg = largeFont.render(
                    "YOU WIN THIS ROUND", 1, (255, 255, 255))
                screen.blit(winmsg, (self.windowWidth/2 - winmsg.get_width() /
                            2, self.windowheight/2 - winmsg.get_height()/2))
            pygame.display.update()
            clock.tick(120)


movingRectangle((0, 0, 255))
