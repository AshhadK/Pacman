import pygame
import random
from settings import *
from player_class import *
from pygame import mixer


vec = pygame.math.Vector2
class Enemy1:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pixPos()
        self.direction = vec(0, 0)
        self.target = None
        self.walkcount = 0
        self.eCount = 0
        self.k = 0
        self.eState = 'down'

    def update(self):
        if self.app.player.scoreStateEnemy == 'false':
            if self.app.stateE1 == 'blinked':
                self.k += 1
                if self.k >= 450:
                    self.app.stateE1 = 'blinked2'
            elif self.app.stateE1 == 'blinked2':
                self.k += 1
                if self.k >= 550:
                    self.app.stateE1 = 'stop'
            elif self.app.stateE1 == 'eaten':
                if self.grid_pos == [11, 15]:
                    self.app.stateE1 = 'stop'


        self.target = self.set_target()
        if self.target != self.grid_pos:
            if self.app.stateE1 == 'eaten':
                self.pix_pos += self.direction * self.app.player.sp
            else:
                self.pix_pos += self.direction * self.app.player.sp1
            if int(self.pix_pos[0] + SPACE // 2) % cell_width == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                    if self.direction == vec(1, 0):
                        self.eState = 'right'
                    if self.direction == vec(-1, 0):
                        self.eState = 'left'
                    self.move()
            if int(self.pix_pos[1] + SPACE // 2) % cell_height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                    if self.direction == vec(0, 1):
                        self.eState = 'down'
                    if self.direction == vec(0, -1):
                        self.eState = 'up'
                    self.move()
        # Setting grid position in reference to pix position
        self.grid_pos[0] = (self.pix_pos[0] - SPACE + cell_width // 2) // cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - SPACE + cell_height // 2) // cell_height + 1




    def draw(self):
        if self.app.stateE1 == 'stop':
            self.k = 0
            self.aaaa = 0
            if self.eState == 'right':
                if self.walkcount + 1 >= 32:
                    self.walkcount = 0
                r = self.app.orangeR[self.walkcount // 8]
                self.app.screen.blit(r, ((int(self.pix_pos.x) - 10, int(self.pix_pos.y) - 10)))
                self.walkcount += 1
            if self.eState == 'left':
                if self.walkcount + 1 >= 32:
                    self.walkcount = 0
                r = self.app.orangeL[self.walkcount // 8]
                self.app.screen.blit(r, ((int(self.pix_pos.x) - 10, int(self.pix_pos.y) - 10)))
                self.walkcount += 1
            if self.eState == 'up':
                if self.walkcount + 1 >= 32:
                    self.walkcount = 0
                r = self.app.orangeU[self.walkcount // 8]
                self.app.screen.blit(r, ((int(self.pix_pos.x) - 10, int(self.pix_pos.y) - 10)))
                self.walkcount += 1
            if self.eState == 'down':
                if self.walkcount + 1 >= 32:
                    self.walkcount = 0
                r = self.app.orangeD[self.walkcount // 8]
                self.app.screen.blit(r, ((int(self.pix_pos.x) - 10, int(self.pix_pos.y) - 10)))
                self.walkcount += 1
        if self.app.stateE1 == 'blinked':
            if self.walkcount + 1 >= 32:
                self.walkcount = 0
            r = self.app.blinkedE[self.walkcount // 8]
            self.app.screen.blit(r, ((int(self.pix_pos.x)-10, int(self.pix_pos.y) - 10)))
            self.walkcount += 1
        if self.app.stateE1 == 'blinked2':
            if self.walkcount + 1 >= 32:
                self.walkcount = 0
            s = self.app.blinkedE2[self.walkcount // 8]
            self.app.screen.blit(s, ((int(self.pix_pos.x) - 10, int(self.pix_pos.y) - 10)))
            self.walkcount += 1
        if self.app.stateE1 == 'eaten':
            self.aaaa +=0.5
            if self.eState == 'right':
                self.app.screen.blit(self.app.eyesR, ((int(self.pix_pos.x)-5, int(self.pix_pos.y)-5)))
            elif self.eState == 'left':
                self.app.screen.blit(self.app.eyesL, ((int(self.pix_pos.x)-5, int(self.pix_pos.y)-5)))
            elif self.eState == 'down':
                self.app.screen.blit(self.app.eyesD, ((int(self.pix_pos.x)-5, int(self.pix_pos.y)-5)))
            else:
                self.app.screen.blit(self.app.eyesU, ((int(self.pix_pos.x)-5, int(self.pix_pos.y)-5)))

    def set_target(self):
        if self.app.stateE1 == 'stop':
            return vec(self.app.player.grid_pos)


        elif self.app.stateE1 == 'blinked' or self.app.stateE1 == 'blinked2' :
            if self.app.player.grid_pos[0] > COLS // 2 and self.app.player.grid_pos[1] > ROWS // 2:
                return vec(1, 1)
            elif self.app.player.grid_pos[0] > COLS // 2 and self.app.player.grid_pos[1] < ROWS // 2:
                return vec(1, ROWS - 2)
            elif self.app.player.grid_pos[0] < COLS // 2 and self.app.player.grid_pos[1] > ROWS // 2:
                return vec(COLS - 2, 1)
            else:
                return vec(COLS - 2, ROWS - 2)

        elif self.app.stateE1 == 'eaten':
            return vec(11,15)


    def timeToMove(self):
        if int(self.pix_pos[0] + SPACE // 2) % cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos[1] + SPACE // 2) % cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True

    def move(self):
        self.direction = self.get_path_direction(self.target)

    def get_path_direction(self, target):
        next_cell = self.find_next_cell_in_path(target)
        xDir = next_cell[0] - self.grid_pos[0]
        yDir = next_cell[1] - self.grid_pos[1]
        return vec(xDir, yDir)

    def find_next_cell_in_path(self, target):
        path = self.BFS([int(self.grid_pos[0]), int(self.grid_pos[1])],[int(target[0]), int(target[1])])
        return path[1]

    def BFS(self, start, target):
        grid = [[0 for x in range(28)] for x in range(30)]
        for cell in self.app.walls:
            if cell.x < 28 and cell.y < 30:
                grid[int(cell.y)][int(cell.x)] = 1
        queue = [start]
        path = []
        visited = []
        while queue:
            current = queue[0]
            queue.remove(queue[0])
            visited.append(current)
            if current == target:
                break
            else:
                neighbours = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                for neighbour in neighbours:
                    if neighbour[0]+current[0] >= 0 and neighbour[0] + current[0] < len(grid[0]):
                        if neighbour[1]+current[1] >= 0 and neighbour[1] + current[1] < len(grid):
                            next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    queue.append(next_cell)
                                    path.append({"Current": current, "Next": next_cell})
        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0, step["Current"])
        return shortest


    def get_pixPos(self):
        return vec(self.grid_pos[0] * cell_width + SPACE // 2 + cell_width // 2,
                   self.grid_pos[1] * cell_height + SPACE // 2 + cell_height // 2)