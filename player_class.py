import pygame
from settings import *
from game_class import *
from pygame import mixer
vec = pygame.math.Vector2
class Player():
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pixPos()
        self.direction = vec(0, 0)
        self.stored_direction = None
        self.moveOrNot = True
        self.k = 0
        self.score = 0
        self.speed = 2
        self.sp1 = 1
        self.sp = 0
        self.lives = 3
        self.walkcount = 0
        self.walkC = 0
        self.level = 1
        self.cherryScore = 150
        self.strawBerryScore = 250
        self.orangeScore = 350
        self.orangeScore_2 = 450
        self.appleScore = 550
        self.appleScore_2 = 650
        self.grapeScore = 750
        self.grapeScore_2 = 850
        self.scoreStateEnemy = 'false'


        #[7, 315]
        #[590,315]
    def update(self):

        if self.score > self.app.h_score:
            self.app.h_score = self.score
        if self.app.pacState == 'out':
            self.app.pacTimer +=1
            self.direction *= 0

        if self.app.pacTimer >= 20:
            self.app.pacState = 'right'
            self.app.player.lives -= 1
            self.app.pacTimer = 0
            self.grid_pos = [13, 23]
            self.pix_pos = self.get_pixPos()
            self.direction *= 0
            self.app.enemy1.grid_pos = [11, 15]
            self.app.enemy1.pix_pos = self.app.enemy1.get_pixPos()
            self.app.enemy1.direction *= 0
            self.app.enemy2.grid_pos = [11, 13]
            self.app.enemy2.pix_pos = self.app.enemy2.get_pixPos()
            self.app.enemy2.direction *= 0
            self.app.enemy3.grid_pos = [16, 13]
            self.app.enemy3.pix_pos = self.app.enemy3.get_pixPos()
            self.app.enemy3.direction *= 0
            self.app.enemy4.grid_pos = [16, 15]
            self.app.enemy4.pix_pos = self.app.enemy4.get_pixPos()
            self.app.enemy4.direction *= 0

        if self.lives == 0:
            self.app.state = 'gameOver'
        self.set_score()

        if self.moveOrNot:
            self.pix_pos += self.direction*self.speed
        if int(self.pix_pos[0] + SPACE // 2) % cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                if (self.stored_direction != None):
                    self.direction = self.stored_direction
                self.moveOrNot = self.can_move()
        if int(self.pix_pos[1] + SPACE // 2) % cell_width == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                if (self.stored_direction != None):
                    self.direction = self.stored_direction
                self.moveOrNot = self.can_move()


            # Setting grid position in reference to pix pos
        self.grid_pos[0] = (self.pix_pos[0] - SPACE + cell_width // 2) // cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - SPACE + cell_height // 2) // cell_height + 1

    def draw(self):

        if self.walkcount + 1 >= 24:
            self.walkcount = 0
        if self.walkC + 1 >= 36:
            self.walkC = 0
        if self.app.pacState == 'right':
            r = self.app.walkRight[self.walkcount // 6]
            self.app.screen.blit(r, ((int(self.pix_pos[0]) - 10, int(self.pix_pos[1]) - 10)))
            self.walkcount += 1
        elif self.app.pacState == 'left':
            l = self.app.walkLeft[self.walkcount // 6]
            self.app.screen.blit(l, ((int(self.pix_pos[0]) - 10, int(self.pix_pos[1]) - 10)))
            self.walkcount += 1
        elif self.app.pacState == 'up':
            u = self.app.walkUp[self.walkcount // 6]
            self.app.screen.blit(u, ((int(self.pix_pos[0]) - 10, int(self.pix_pos[1]) - 10)))
            self.walkcount += 1
        elif self.app.pacState == 'down':
            d = self.app.walkDown[self.walkcount // 6]
            self.app.screen.blit(d, ((int(self.pix_pos[0]) - 10, int(self.pix_pos[1]) - 10)))
            self.walkcount += 1
        if self.app.pacState == 'out':
            out = self.app.pacOut[self.walkC // 9]
            self.app.screen.blit(out, ((int(self.pix_pos[0]) - 10, int(self.pix_pos[1]) - 10)))
            self.walkC += 1
            #pygame.draw.rect(self.app.screen,RED,(int(self.pix_pos[0])-10, int(self.pix_pos[1])-10,20,20),1)
            # Drawing the grid pos rect
           ## pygame.draw.rect(self.app.screen, RED, (self.grid_pos[0]*cell_width+SPACE//2,self.grid_pos[1]*cell_height+SPACE//2, cell_width, cell_height), 1)

    def draw_2(self):
        self.app.draw_text(f"{self.app.eatenScore}", self.app.screen,((int(self.pix_pos[0]) - 10, int(self.pix_pos[1]) - 10)),
                               12, WHITE, START_FONT)

    def update_2(self):
        self.sp = 0
        self.sp1 = 0
        self.app.blinkedScoreTimer += 1
        self.pix_pos += self.direction * 0
        if self.app.blinkedScoreTimer > 50:
            self.app.blinkedScoreTimer = 0
            self.scoreStateEnemy = 'false'
            self.sp = 2
            self.sp1 = 1




    def move(self,direction):
        self.stored_direction = direction

    def get_pixPos(self):
        return vec(self.grid_pos[0] * cell_width + SPACE//2+cell_width//2, self.grid_pos[1] * cell_height + SPACE//2+cell_height//2)

    def onCoin(self):
        self.eat_coin()
        self.eat_pellets()

        if (self.app.pelletsList == [] and self.app.coinsList == []):
            self.app.coinsEaten = 'true'

    def eat_fruit(self):
        if (self.app.fruitPos == self.grid_pos):
            self.app.scoreState = 'true'
            self.app.scoreTimer *= 0
            if self.app.player.level == 1:
                self.score += self.cherryScore
                self.app.tim *= 0

            if self.app.player.level == 2:
                self.score += self.strawBerryScore
                self.app.tim *= 0

            if self.app.player.level == 3:
                self.score += self.orangeScore
                self.app.tim *= 0

            if self.app.player.level == 4:
                self.score += self.orangeScore_2
                self.app.tim *= 0

            if self.app.player.level == 5 :
                self.score += self.appleScore
                self.app.tim *= 0

            if self.app.player.level == 6 :
                self.score += self.appleScore_2
                self.app.tim *= 0

            if self.app.player.level == 7 :
                self.score += self.grapeScore
                self.app.tim *= 0

            if self.app.player.level == 8 :
                self.score += self.grapeScore_2
                self.app.tim *= 0


    def eat_coin(self):
        if self.grid_pos in self.app.coinsList:
            if self.timeToMove():
                self.score += 10
                #self.app.pacEatPellets.play()
                self.app.coinsList.remove(self.grid_pos)

    def eat_pellets(self):
        if self.grid_pos in self.app.pelletsList:
            if self.timeToMove():
                if self.app.stateE1 == 'stop':
                    self.app.stateE1 = 'blinked'
                if self.app.stateE2 == 'stop':
                    self.app.stateE2 = 'blinked'
                if self.app.stateE3 == 'stop':
                    self.app.stateE3 = 'blinked'
                if self.app.stateE4 == 'stop':
                    self.app.stateE4 = 'blinked'
                self.score += 10
                self.app.pelletsList.remove(self.grid_pos)


    def timeToMove(self):
        if int(self.pix_pos[0] + SPACE // 2) % cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos[1] + SPACE // 2) % cell_width == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True

    def can_move(self):
        for a in self.app.walls:
            if vec(self.grid_pos+self.direction)==a:
                return False
        return True

    def set_score(self):
        if self.app.num <= 50:
            self.app.eatenScore = 200
        elif self.app.num <= 100:
            self.app.eatenScore = 400
        elif self.app.num <= 150:
            self.app.eatenScore = 800
        elif self.app.num <= 200:
            self.app.eatenScore = 1600



