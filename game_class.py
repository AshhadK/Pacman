from player_class import Player
from settings import *
from enemy_class import *
from enemy_class2 import *
from enemy_class3 import *
from enemy_class4 import *
import pydub


import time

import pygame, sys
from pygame import mixer

pygame.init()

vec = pygame.math.Vector2


class App():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("PACMAN")
        self.clock = pygame.time.Clock()
        self.running = True
        self.h_score = 0
        self.kap = 0
        self.walkcount = 0
        self.wal = 0
        self.state = 'start'
        self.pacState = 'right'
        self.stateE1 = 'stop'
        self.stateE2 = 'stop'
        self.stateE3 = 'stop'
        self.stateE4 = 'stop'
        self.winTimer = 0
        self.colorState = 'startYellow'
        self.scoreState = 'false'
        self.coinsEaten = 'false'
        self.e4X = -25
        self.e3X = -55
        self.e2X = -85
        self.e1X = -115
        self.bX = 550
        self.pX = 20
        self.sp1 = 1.5
        self.sp2 = 1
        self.num = 0
        self.walls = []
        self.tim = 0
        self.walk = 0
        self.scoreTimer = 0
        self.blinkedScoreTimer = 0
        self.pacTimer = 0
        self.coinsList = []
        self.pelletsList = []
        self.blackPos = []
        self.a = []
        self.b = []
        self.c = []
        self.d = []
        self.e1 = None
        self.e2 = None
        self.e3 = None
        self.e4 = None
        self.fruitPos = None
        self.loadImages()
        self.enemy1 = Enemy1(self, self.e1)
        self.enemy2 = Enemy2(self, self.e2)
        self.enemy3 = Enemy3(self, self.e3)
        self.enemy4 = Enemy4(self, self.e4)
        self.l = 0
        self.player = Player(self,playerStartPos)
        self.eatenScore = 0
        for i in range(500, 100000, 1000):
            self.a.append(i)
        print(self.a)
        for i in range(1000, 100000, 1000):
            self.b.append(i)
        print(self.b)
        for i in range(10, 10000, 40):
            self.c.append(i)
        print(self.c)
        for i in range(40, 10000, 40):
            self.d.append(i)
        print(self.d)


    def run(self):
        while (self.running):
            self.clock.tick(FPS)
            if (self.state == 'start'):
                self.l = 0
                self.start_events()
                self.start_update()
                self.start_draw()

            elif (self.state == 'playing'):
                self.playing_events()
                self.l += (0.5)
                self.playing_update()
                self.playing_draw()
            elif(self.state == 'gameOver'):
                self.l = 0

                self.gameOver_events()


            else:
                pass
        pygame.quit()
        sys.exit()
    ###########################MAINWINDOW ###########################
    def draw_text(self,f_text,screen,position,size,color,f_name):
        font = pygame.font.SysFont(f_name,size)
        text = font.render(f_text,False,color)
        screen.blit(text,position)
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.colorState = 'startYellow'
            if keys[pygame.K_DOWN]:
                self.colorState = 'creditsYellow'
            if keys[pygame.K_SPACE] and self.colorState == 'startYellow':
                self.state = 'playing'
                pygame.mixer.music.load("MUSIC/game_start.wav")
                pygame.mixer.music.play()

    def start_update(self):
        self.l += (0.5)

        if self.pacState == 'right':
            self.pX += self.sp1
            self.e1X += self.sp1
            self.e2X += self.sp1
            self.e3X += self.sp1
            self.e4X += self.sp1
            if self.pX > 550:
                self.pX = 550
                self.pacState = 'left'
                self.bX = -1000

        if self.pacState == 'left':
            self.pX -= self.sp1
            self.e1X -= self.sp2
            self.e2X -= self.sp2
            self.e3X -= self.sp2
            self.e4X -= self.sp2
            if self.pX == self.e1X:
                aunty = self.e1X
                if self.e1X == aunty:
                    self.screen.blit(self.pacR, (aunty, 350))
                pygame.time.delay(200)
                self.e1X = -1000
            if self.pX == self.e2X:
                pygame.time.delay(200)
                self.e2X = -1000
            if self.pX == self.e3X:
                pygame.time.delay(200)
                self.e3X = -1000
            if self.pX == self.e4X:
                pygame.time.delay(200)
                self.e4X = -1000
            if self.pX < -60:
                self.pacState = 'right'
                self.e4X = -25
                self.e3X = -55
                self.e2X = -85
                self.e1X = -115
                self.bX = 550
                self.pX = 20
        self.kap+=1
        pygame.display.update()

    def start_draw(self):
        self.screen.fill(BLACK)
        if self.colorState == 'startYellow':
            self.screen.blit(self.backGround1,(0,0))
        if self.colorState == 'creditsYellow':
            self.screen.blit(self.backGround2,(0,0))
        self.draw_text(f"HIGH SCORE : {self.h_score}", self.screen, (420, 5), 18, ghostOrange, "ravie")

        if self.kap % 64 in range(32):
            self.screen.blit(self.blink, (self.bX, 353))

        if self.walkcount + 1 >= 24:
            self.walkcount = 0
        if self.walkcount + 1 >= 24:
            self.walkcount = 0
        if self.pacState == 'right':
            r = self.walkRight[self.walkcount // 6]            
            s = self.blueR[self.walkcount // 6]
            t = self.pinkR[self.walkcount // 6]
            u = self.redR[self.walkcount // 6]
            v = self.orangeR[self.walkcount // 6]
            self.screen.blit(r, (self.pX,350))
            self.screen.blit(s, (self.e1X, 350))
            self.screen.blit(t, (self.e2X, 350))
            self.screen.blit(u, (self.e3X, 350))
            self.screen.blit(v, (self.e4X, 350))
            self.walkcount += 1
            
        elif self.pacState == 'left':
            r = self.walkLeft[self.walkcount // 6]
            s = self.blinkedE[self.walkcount // 6]
            self.screen.blit(r, (self.pX, 350))
            self.screen.blit(s, (self.e1X, 350))
            self.screen.blit(s, (self.e2X, 350))
            self.screen.blit(s, (self.e3X, 350))
            self.screen.blit(s, (self.e4X, 350))
            self.walkcount += 1
        #self.draw_text("PUSH SPACEBAR TO START",self.screen,[WIDTH/4,HEIGHT/2.8],START_TEXT_SIZE,(170,132,58),START_FONT)
        #self.draw_text("1 PLAYER ONLY", self.screen, [WIDTH / 4+50, HEIGHT / 2.8 + 150], START_TEXT_SIZE,
                       #(50, 150, 255), START_FONT)
        #self.draw_text("HIGH SCORE", self.screen, [10,10], START_TEXT_SIZE,
                       #(255,255,255), START_FONT)



    ###########################PLAY
 ###########################PLAYING SCREEN###########################
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.pacState = 'right'
                self.player.move(vec(1,0))
            elif keys[pygame.K_LEFT]:
                self.pacState = 'left'
                self.player.move(vec(-1, 0))
            elif keys[pygame.K_UP]:
                self.pacState = 'up'
                self.player.move(vec(0, -1))
            elif keys[pygame.K_DOWN]:
                self.pacState = 'down'
                self.player.move(vec(0, 1))

    def loadImages(self):
        self.bg = pygame.image.load('ITEMS/maze.png').convert()
        self.bg = pygame.transform.scale(self.bg,(MAZE_WIDTH,MAZE_HEIGHT))
        self.bg3 = pygame.image.load('ITEMS/maze3.jpg')
        self.bg4 = pygame.image.load('ITEMS/maze4.jpg')
        self.bg2 = [pygame.image.load('ITEMS/maze2.jpg'),self.bg,pygame.image.load('ITEMS/maze2.jpg')
                    ,self.bg,pygame.image.load('ITEMS/maze2.jpg'),self.bg]
        self.bg5 = [pygame.image.load('ITEMS/maze2.jpg'), self.bg3, pygame.image.load('ITEMS/maze2.jpg')
            , self.bg3, pygame.image.load('ITEMS/maze2.jpg'), self.bg3]
        self.bg6 = [pygame.image.load('ITEMS/maze2.jpg'), self.bg4, pygame.image.load('ITEMS/maze2.jpg')
            , self.bg4, pygame.image.load('ITEMS/maze2.jpg'), self.bg4]
        self.gameover = pygame.image.load('ITEMS/gameover.PNG')
        self.start = pygame.image.load('ITEMS/getready.PNG')
        self.levelPic = pygame.image.load('ITEMS/level.jpg')
        self.win = pygame.image.load('ITEMS/gamewin1.bmp')
        self.score = pygame.image.load('ITEMS/score.bmp')
        self.cage = pygame.image.load('ITEMS/ek.jpg')
        self.apple = pygame.image.load('ITEMS/apple.jpg')
        self.backGround1 = pygame.image.load('ITEMS/background1.jpg')
        self.backGround2 = pygame.image.load('ITEMS/background2.jpg')
        self.grapes = pygame.image.load('ITEMS/grapes.jpg')
        self.cherry = pygame.image.load('ITEMS/cherry.jpg')
        self.strawberry = pygame.image.load('ITEMS/strawberry.jpg')
        self.orange = pygame.image.load('ITEMS/orange.jpg')
        self.blink = pygame.image.load('ITEMS/dotWhite.jpg')
        self.walkRight = [pygame.image.load('PLAYER/pac1.jpg'), pygame.image.load('PLAYER/pac2.jpg'), pygame.image.load('PLAYER/pac3.jpg'),
                          pygame.image.load('PLAYER/pac4.jpg'), pygame.image.load('PLAYER/pac5.jpg'), pygame.image.load('PLAYER/pac1.jpg')]
        self.walkLeft = [pygame.image.load('PLAYER/pac1.jpg'), pygame.image.load('PLAYER/pacL2.jpg'), pygame.image.load('PLAYER/pacL3.jpg'),
                         pygame.image.load('PLAYER/pacL4.jpg'), pygame.image.load('PLAYER/pacL5.jpg'), pygame.image.load('PLAYER/pac1.jpg')]
        self.walkUp = [pygame.image.load('PLAYER/pac1.jpg '), pygame.image.load('PLAYER/pacU2.jpg '), pygame.image.load('PLAYER/pacU3.jpg'),
                       pygame.image.load('PLAYER/pacU4.jpg '), pygame.image.load('PLAYER/pacU5.jpg '), pygame.image.load('PLAYER/pac1.jpg')]
        self.walkDown = [pygame.image.load('PLAYER/pac1.jpg '), pygame.image.load('PLAYER/pacD2.jpg '), pygame.image.load('PLAYER/pacD3.jpg'),
                         pygame.image.load('PLAYER/pacD4.jpg '), pygame.image.load('PLAYER/pacD5.jpg '), pygame.image.load('PLAYER/pac1.jpg')]
        self.pinkR = [pygame.image.load('ENEMIES/pinkR1.png'), pygame.image.load('ENEMIES/pinkR0.png'),
                      pygame.image.load('ENEMIES/pinkR1.png'), pygame.image.load('ENEMIES/pinkR0.png'),
                      pygame.image.load('ENEMIES/pinkR1.png'), pygame.image.load('ENEMIES/pinkR0.png'),
                      pygame.image.load('ENEMIES/pinkR1.png'), pygame.image.load('ENEMIES/pinkR0.png')]
        self.pinkL = [pygame.image.load('ENEMIES/pinkL1.png'), pygame.image.load('ENEMIES/pinkL0.png'),
                      pygame.image.load('ENEMIES/pinkL1.png'), pygame.image.load('ENEMIES/pinkL0.png'),
                      pygame.image.load('ENEMIES/pinkL1.png'), pygame.image.load('ENEMIES/pinkL0.png'),
                      pygame.image.load('ENEMIES/pinkL1.png'), pygame.image.load('ENEMIES/pinkL0.png')]
        self.pinkD = [pygame.image.load('ENEMIES/pinkD1.png'), pygame.image.load('ENEMIES/pinkD0.png'),
                      pygame.image.load('ENEMIES/pinkD1.png'), pygame.image.load('ENEMIES/pinkD0.png'),
                      pygame.image.load('ENEMIES/pinkD1.png'), pygame.image.load('ENEMIES/pinkD0.png'),
                      pygame.image.load('ENEMIES/pinkD1.png'), pygame.image.load('ENEMIES/pinkD0.png')]
        self.pinkU = [pygame.image.load('ENEMIES/pinkU1.png'), pygame.image.load('ENEMIES/pinkU0.png'),
                      pygame.image.load('ENEMIES/pinkU1.png'), pygame.image.load('ENEMIES/pinkU0.png'),
                      pygame.image.load('ENEMIES/pinkU1.png'), pygame.image.load('ENEMIES/pinkU0.png'),
                      pygame.image.load('ENEMIES/pinkU1.png'), pygame.image.load('ENEMIES/pinkU0.png')]
        self.redR = [pygame.image.load('ENEMIES/redR1.png'), pygame.image.load('ENEMIES/redR0.png'),
                     pygame.image.load('ENEMIES/redR1.png'), pygame.image.load('ENEMIES/redR0.png'),
                     pygame.image.load('ENEMIES/redR1.png'), pygame.image.load('ENEMIES/redR0.png'),
                     pygame.image.load('ENEMIES/redR1.png'), pygame.image.load('ENEMIES/redR0.png')]
        self.redL = [pygame.image.load('ENEMIES/redL1.png'), pygame.image.load('ENEMIES/redL0.png'),
                     pygame.image.load('ENEMIES/redL1.png'), pygame.image.load('ENEMIES/redL0.png'),
                     pygame.image.load('ENEMIES/redL1.png'), pygame.image.load('ENEMIES/redL0.png'),
                     pygame.image.load('ENEMIES/redL1.png'), pygame.image.load('ENEMIES/redL0.png')]
        self.redD = [pygame.image.load('ENEMIES/redD1.png'), pygame.image.load('ENEMIES/redD0.png'),
                     pygame.image.load('ENEMIES/redD1.png'), pygame.image.load('ENEMIES/redD0.png'),
                     pygame.image.load('ENEMIES/redD1.png'), pygame.image.load('ENEMIES/redD0.png'),
                     pygame.image.load('ENEMIES/redD1.png'), pygame.image.load('ENEMIES/redD0.png')]
        self.redU = [pygame.image.load('ENEMIES/redU1.png'), pygame.image.load('ENEMIES/redU0.png'),
                     pygame.image.load('ENEMIES/redU1.png'), pygame.image.load('ENEMIES/redU0.png'),
                     pygame.image.load('ENEMIES/redU1.png'), pygame.image.load('ENEMIES/redU0.png'),
                     pygame.image.load('ENEMIES/redU1.png'), pygame.image.load('ENEMIES/redU0.png')]
        self.orangeR = [pygame.image.load('ENEMIES/orangeR1.png'), pygame.image.load('ENEMIES/orangeR0.png'),
                        pygame.image.load('ENEMIES/orangeR1.png'), pygame.image.load('ENEMIES/orangeR0.png'),
                        pygame.image.load('ENEMIES/orangeR1.png'), pygame.image.load('ENEMIES/orangeR0.png'),
                        pygame.image.load('ENEMIES/orangeR1.png'), pygame.image.load('ENEMIES/orangeR0.png')]
        self.orangeL = [pygame.image.load('ENEMIES/orangeL1.png'), pygame.image.load('ENEMIES/orangeL0.png'),
                        pygame.image.load('ENEMIES/orangeL1.png'), pygame.image.load('ENEMIES/orangeL0.png'),
                        pygame.image.load('ENEMIES/orangeL1.png'), pygame.image.load('ENEMIES/orangeL0.png'),
                        pygame.image.load('ENEMIES/orangeL1.png'), pygame.image.load('ENEMIES/orangeL0.png')]
        self.orangeD = [pygame.image.load('ENEMIES/orangeD1.png'), pygame.image.load('ENEMIES/orangeD0.png'),
                        pygame.image.load('ENEMIES/orangeD1.png'), pygame.image.load('ENEMIES/orangeD0.png'),
                        pygame.image.load('ENEMIES/orangeD1.png'), pygame.image.load('ENEMIES/orangeD0.png'),
                        pygame.image.load('ENEMIES/orangeD1.png'), pygame.image.load('ENEMIES/orangeD0.png')]
        self.orangeU = [pygame.image.load('ENEMIES/orangeU1.png'), pygame.image.load('ENEMIES/orangeU0.png'),
                        pygame.image.load('ENEMIES/orangeU1.png'), pygame.image.load('ENEMIES/orangeU0.png'),
                        pygame.image.load('ENEMIES/orangeU1.png'), pygame.image.load('ENEMIES/orangeU0.png'),
                        pygame.image.load('ENEMIES/orangeU1.png'), pygame.image.load('ENEMIES/orangeU0.png')]
        self.blueR = [pygame.image.load('ENEMIES/blueR1.png'), pygame.image.load('ENEMIES/blueR0.png'),
                      pygame.image.load('ENEMIES/blueR1.png'), pygame.image.load('ENEMIES/blueR0.png'),
                      pygame.image.load('ENEMIES/blueR1.png'), pygame.image.load('ENEMIES/blueR0.png'),
                      pygame.image.load('ENEMIES/blueR1.png'), pygame.image.load('ENEMIES/blueR0.png')]
        self.blueL = [pygame.image.load('ENEMIES/blueL1.png'), pygame.image.load('ENEMIES/blueL0.png'),
                      pygame.image.load('ENEMIES/blueL1.png'), pygame.image.load('ENEMIES/blueL0.png'),
                      pygame.image.load('ENEMIES/blueL1.png'), pygame.image.load('ENEMIES/blueL0.png'),
                      pygame.image.load('ENEMIES/blueL1.png'), pygame.image.load('ENEMIES/blueL0.png')]
        self.blueD = [pygame.image.load('ENEMIES/blueD1.png'), pygame.image.load('ENEMIES/blueD0.png'),
                      pygame.image.load('ENEMIES/blueD1.png'), pygame.image.load('ENEMIES/blueD0.png'),
                      pygame.image.load('ENEMIES/blueD1.png'), pygame.image.load('ENEMIES/blueD0.png'),
                      pygame.image.load('ENEMIES/blueD1.png'), pygame.image.load('ENEMIES/blueD0.png')]
        self.blueU = [pygame.image.load('ENEMIES/blueU1.png'), pygame.image.load('ENEMIES/blueU0.png'),
                      pygame.image.load('ENEMIES/blueU1.png'), pygame.image.load('ENEMIES/blueU0.png'),
                      pygame.image.load('ENEMIES/blueU1.png'), pygame.image.load('ENEMIES/blueU0.png'),
                      pygame.image.load('ENEMIES/blueU1.png'), pygame.image.load('ENEMIES/blueU0.png')]
        self.blinkedE = [pygame.image.load('ENEMIES/ghostBlinked1.png'),pygame.image.load('ENEMIES/ghostBlinked.png'),
                        pygame.image.load('ENEMIES/ghostBlinked1.png'), pygame.image.load('ENEMIES/ghostBlinked.png'),
                        pygame.image.load('ENEMIES/ghostBlinked1.png'), pygame.image.load('ENEMIES/ghostBlinked.png'),
                        pygame.image.load('ENEMIES/ghostBlinked1.png'), pygame.image.load('ENEMIES/ghostBlinked.png')]
        self.blinkedE2 = [pygame.image.load('ENEMIES/ghostBlinkBlue1.jpg'), pygame.image.load('ENEMIES/ghostBlinkBlue.jpg'),
                         pygame.image.load('ENEMIES/ghostBlinked1.png'), pygame.image.load('ENEMIES/ghostBlinked.png'),
                          pygame.image.load('ENEMIES/ghostBlinkBlue1.jpg'), pygame.image.load('ENEMIES/ghostBlinkBlue.jpg'),
                          pygame.image.load('ENEMIES/ghostBlinked1.png'), pygame.image.load('ENEMIES/ghostBlinked.png')]

        self.eyesR = pygame.image.load('ENEMIES/eyesR.png')
        self.eyesL = pygame.image.load('ENEMIES/eyesL.png')
        self.eyesU = pygame.image.load('ENEMIES/eyesU.png')
        self.eyesD = pygame.image.load('ENEMIES/eyesD.png')

        self.pacOut = [pygame.image.load('PLAYER/pac1.jpg '),pygame.image.load('PLAYER/out1.jpg '),pygame.image.load('PLAYER/out1.jpg '),
                       pygame.image.load('PLAYER/out2.jpg '), pygame.image.load('PLAYER/out2.jpg'),pygame.image.load('PLAYER/out3.jpg '),
                       pygame.image.load('PLAYER/out3.jpg'),pygame.image.load('PLAYER/out4.jpg'),pygame.image.load('PLAYER/out4.jpg')]
        self.pacR = pygame.image.load('PLAYER/pac4.jpg ')
        self.pacL = pygame.image.load('PLAYER/pacL4.jpg ')
        self.pacU = pygame.image.load('PLAYER/pacU4.jpg ')
        self.pacD = pygame.image.load('PLAYER/pacD4.jpg ')

        ##self.coinImage = pygame.image.load('pill.png').convert()

        with open("walls.txt",'r') as file:
            for yIndex,line in enumerate(file):
                for xIndex,char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xIndex,yIndex))
                    elif char == "C":
                        self.coinsList.append(vec(xIndex,yIndex))
                    elif char == "E":
                        self.pelletsList.append(vec(xIndex,yIndex))
                    elif char in ['B']:
                        self.e1 = [xIndex,yIndex]
                        print('e1 = ', self.e1)
                    elif char in ['G']:
                        self.e2 = [xIndex, yIndex]
                        print('e2 = ', self.e2)
                    elif char in ['Y']:
                        self.e3 = [xIndex,yIndex]
                        print('e3 = ',self.e3)
                    elif char in ['R']:
                        self.e4 = [xIndex, yIndex]
                        print('e4 = ', self.e4)
                    elif char == 'W':
                        self.blackPos.append(vec(xIndex,yIndex))
                    elif char in ['F']:
                        self.fruitPos = [xIndex, yIndex]
                        print('fruotPos = ', self.fruitPos)



    def draw_grid(self):
        for x in range(MAZE_WIDTH//cell_width):
           pygame.draw.line(self.bg,GREY,(x*cell_width,0),(x*cell_height,MAZE_HEIGHT))
        for x in range(MAZE_HEIGHT // cell_height):
           pygame.draw.line(self.bg,GREY,(0,x*cell_width),(MAZE_HEIGHT,x*cell_height))
        for a in self.walls:
            pygame.draw.rect(self.bg,(102,82,190),(a.x*cell_width,a.y*cell_height,cell_width,cell_height))

    def playing_draw(self):
        self.screen.fill(BLACK)
        if self.coinsEaten == 'true':
            self.winTimer += 1
            if self.winTimer < 80:
                if self.wal + 1 >= 24:
                    self.wal = 0
                if self.player.level < 3:
                    r = self.bg2[self.wal // 6]
                    self.screen.blit(r, (SPACE // 2, SPACE // 2))
                    self.wal += 1
                    self.screen.blit(self.win, x)
                elif self.player.level >= 3 and self.player.level < 6:
                    r = self.bg5[self.wal // 6]
                    self.screen.blit(r, (SPACE // 2, SPACE // 2))
                    self.wal += 1
                    self.screen.blit(self.win, x)
                else:
                    r = self.bg6[self.wal // 6]
                    self.screen.blit(r, (SPACE // 2, SPACE // 2))
                    self.wal += 1
                    self.screen.blit(self.win, x)


                self.screen.blit(self.cage, (271, 265))

            else:
                self.player.level += 1
                self.reset_2()
        else:
            self.winTimer = 0
            if self.player.level < 3:
                self.screen.blit(self.bg, (SPACE // 2, SPACE // 2))
            elif self.player.level >= 3 and self.player.level < 6:
                self.screen.blit(self.bg3, (SPACE // 2, SPACE // 2))
            else:
                self.screen.blit(self.bg4,(SPACE // 2, SPACE // 2))
        self.screen.blit(self.cage,(271,265))
        #self.draw_grid()
        self.draw_coins()


        self.screen.blit(self.score,(30,4))
        self.draw_text(f"{self.player.score}", self.screen, (98,4), 18,PLAYER_COLOUR, 'ravie')
        #self.drawBlack_Box()
        if self.player.level == 1:
            self.screen.blit(self.cherry, (WIDTH - 60, HEIGHT - 25))
        if self.player.level == 2:
            self.screen.blit(self.cherry, (WIDTH - 60, HEIGHT - 25))
            self.screen.blit(self.strawberry, (WIDTH - 85, HEIGHT - 25))
        if self.player.level == 3 or self.player.level == 4:
            self.screen.blit(self.cherry, (WIDTH - 60, HEIGHT - 25))
            self.screen.blit(self.strawberry, (WIDTH - 85, HEIGHT - 25))
            self.screen.blit(self.orange, (WIDTH - 110, HEIGHT - 25))
        if self.player.level == 5 or self.player.level == 6:
            self.screen.blit(self.cherry, (WIDTH - 60, HEIGHT - 25))
            self.screen.blit(self.strawberry, (WIDTH - 85, HEIGHT - 25))
            self.screen.blit(self.orange, (WIDTH - 110, HEIGHT - 25))
            self.screen.blit(self.apple, (WIDTH - 135, HEIGHT - 25))
        if self.player.level == 7 or self.player.level == 8:
            self.screen.blit(self.cherry, (WIDTH - 60, HEIGHT - 25))
            self.screen.blit(self.strawberry, (WIDTH - 85, HEIGHT - 25))
            self.screen.blit(self.orange, (WIDTH - 110, HEIGHT - 25))
            self.screen.blit(self.apple, (WIDTH - 135, HEIGHT - 25))
            self.screen.blit(self.grapes, (WIDTH - 160, HEIGHT - 25))

        for i in range(self.player.lives-1):
            self.screen.blit(self.pacR, (35 + 25 * i, HEIGHT - 25))


        if self.scoreState == 'false':
            self.draw_fruit()
        elif self.scoreState == 'true':
            self.draw_score()
        if self.pacState != 'out' and self.state!= 'gameOver' and self.coinsEaten == 'false':
            self.enemy1.draw()
            self.enemy2.draw()
            self.enemy3.draw()
            #self.scoreBlit()
            self.enemy4.draw()

        if self.player.scoreStateEnemy == 'false' and self.state!= 'gameOver' and self.coinsEaten == 'false':
            self.player.draw()
        elif self.player.scoreStateEnemy == 'true':
            self.player.draw_2()

        if self.state == 'gameOver':
            self.screen.blit(self.gameover,x)

        pygame.display.update()

    def playing_update(self):
        self.tim +=1
        if self.l > 40:
            if self.player.scoreStateEnemy == 'false' and self.state!= 'gameOver'and self.coinsEaten == 'false':
                self.player.update()
            elif self.player.scoreStateEnemy == 'true':
                self.player.update_2()

            self.player.onCoin()

            if self.state != 'gameOver' and self.coinsEaten == 'false':
                self.enemy1.update()
                self.enemy2.update()
                self.enemy3.update()
                self.enemy4.update()
        if(self.stateE1 == 'stop'):
            if self.enemy1.grid_pos == self.player.grid_pos:
                if int(self.player.pix_pos[0] + SPACE // 2) % cell_width == 0:
                    if self.player.timeToMove():
                        self.remove_lives()

        if (self.stateE2 == 'stop'):
            if self.enemy2.grid_pos == self.player.grid_pos:
                if int(self.player.pix_pos[0] + SPACE // 2) % cell_width == 0:
                    if self.player.timeToMove():
                        self.remove_lives()

        if (self.stateE3 == 'stop'):
            if self.enemy3.grid_pos == self.player.grid_pos:
                if int(self.player.pix_pos[0] + SPACE // 2) % cell_width == 0:
                    if self.player.timeToMove():
                        self.remove_lives()

        if (self.stateE4 == 'stop'):
            if self.enemy4.grid_pos == self.player.grid_pos:
                if int(self.player.pix_pos[0] + SPACE // 2) % cell_width == 0:
                    if self.player.timeToMove():
                        self.remove_lives()


        if self.enemy1.grid_pos == self.player.grid_pos or self.enemy2.grid_pos == self.player.grid_pos or self.enemy3.grid_pos == self.player.grid_pos or self.enemy4.grid_pos == self.player.grid_pos:
            self.num += 1

        if self.stateE1 == 'stop' and self.stateE2 == 'stop' and self.stateE3 == 'stop' and self.stateE4 == 'stop':
            self.num = 0

        if (self.stateE1 == 'blinked' or self.stateE1 == 'blinked2'):
            if self.enemy1.grid_pos == self.player.grid_pos:
                self.player.scoreStateEnemy = 'true'
                self.stateE1 = 'eaten'
                self.enemy1.pix_pos = self.enemy1.get_pixPos()
                self.player.score += self.eatenScore


                        # self.pacDeath.play()
        if (self.stateE2 == 'blinked' or self.stateE2 == 'blinked2'):
            if self.enemy2.grid_pos == self.player.grid_pos:
                self.player.scoreStateEnemy = 'true'
                self.stateE2 = 'eaten'
                self.enemy2.pix_pos = self.enemy2.get_pixPos()
                self.player.score += self.eatenScore


                        # self.pacDeath.play()
        if (self.stateE3 == 'blinked' or self.stateE3 == 'blinked2'):
            if self.enemy3.grid_pos == self.player.grid_pos:
                self.player.scoreStateEnemy = 'true'
                self.stateE3 = 'eaten'
                self.enemy3.pix_pos = self.enemy3.get_pixPos()
                self.player.score += self.eatenScore


                        # self.pacDeath.play()
        if (self.stateE4 == 'blinked' or self.stateE4 == 'blinked2'):
            if self.enemy4.grid_pos == self.player.grid_pos:
                self.player.scoreStateEnemy = 'true'
                self.stateE4 = 'eaten'
                self.enemy4.pix_pos = self.enemy4.get_pixPos()
                self.player.score += self.eatenScore
                        # self.pacDeath.play()
    def remove_lives(self):
        self.pacState = 'out'
        self.stateE1 = 'stop'
        self.stateE2 = 'stop'
        self.stateE3 = 'stop'
        self.stateE4 = 'stop'
        self.tim *= 0



        # self.pacDeath.play()

    ##  self.coinsList.pop()
    def draw_score(self):
        self.scoreTimer += 1
        self.fruitPos_x = int(self.fruitPos[0] * cell_width + 25)
        self.fruitPos_y = int(self.fruitPos[1] * cell_height + 25)

        if self.player.level == 1:
            self.sc = self.player.cherryScore
        if self.player.level == 2:
            self.sc = self.player.strawBerryScore
        if self.player.level == 3:
            self.sc = self.player.orangeScore
        if self.player.level == 4:
            self.sc = self.player.orangeScore_2
        if self.player.level == 5:
            self.sc = self.player.appleScore
        if self.player.level == 6:
            self.sc = self.player.appleScore_2
        if self.player.level == 7:
            self.sc = self.player.grapeScore
        if self.player.level == 8:
            self.sc = self.player.grapeScore_2

        self.draw_text(f"{self.sc}", self.screen, (self.fruitPos_x-5, self.fruitPos_y-20), 12,
                           WHITE, START_FONT)
        if self.scoreTimer < 50:
            self.scoreState = 'true'
        else:
            self.scoreState = 'false'



    def draw_fruit(self):
        if self.player.level == 1:
            self.fruit = self.cherry
        if self.player.level == 2:
            self.fruit = self.strawberry

        if self.player.level == 3 or self.player.level == 4:
            self.fruit = self.orange

        if self.player.level == 5 or self.player.level == 6:
            self.fruit = self.apple
        if self.player.level == 7 or self.player.level == 8:
            self.fruit = self.grapes
        for i in range(10):
            self.r = self.a[i]
            self.s = self.b[i]
            if self.tim >= self.r and self.tim <= self.s:
                self.player.eat_fruit()
                self.fruitPos_x = int(self.fruitPos[0] * cell_width + 25)
                self.fruitPos_y = int(self.fruitPos[1] * cell_height + 25)
                self.screen.blit(self.fruit, (self.fruitPos_x, self.fruitPos_y))


    def draw_coins(self):
        for a in self.coinsList:
            self.coinPos_x = int(a.x*cell_width+cell_width*2-cell_width//4)
            self.coinPos_y = int(a.y * cell_height + cell_height*2-cell_width//4)
            self.coinGrid = vec(self.coinPos_x,self.coinPos_y)
            self.coinWidth = 2
            pygame.draw.circle(self.screen, PELLET_COLOR,(self.coinPos_x,self.coinPos_y),self.coinWidth)
        for b in self.pelletsList:
            self.coinPos_x = int(b.x * cell_width + cell_width * 2 - cell_width // 4)
            self.coinPos_y = int(b.y * cell_height + cell_height * 2 - cell_height // 4)
            self.coinWidth = 7
            if self.l < 20:
                self.screen.blit(self.levelPic,(270, 365))
                self.draw_text(f"{self.player.level}", self.screen,(330, 367), 18, ghostOrange, "ravie")

            elif self.l > 20 and self.l < 50:
                self.screen.blit(self.start, x)
            for i in range(len(self.d)):
                self.r = self.c[i]
                self.s = self.d[i]
                if self.l > self.r and self.l < self.s:
                    self.screen.blit(self.blink,(self.coinPos_x-6, self.coinPos_y-7))

    def drawBlack_Box(self):
        for blackBox in self.blackPos:
            pygame.draw.rect(self.bg,BLACK,(blackBox.x*cell_width,blackBox.y*cell_height,cell_width,cell_height))



        ##########################GAMEOVERWINDOW ###########################
    def gameOver_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.reset()
                self.state = 'start'
            if keys[pygame.K_ESCAPE]:
                self.running = False

    def gameOver_update(self):
        pass




    def reset(self):
        self.tim *= 0
        self.player.lives = 3
        self.player.score = 0
        self.coinsList = []
        self.pelletsList =[]
        self.player.grid_pos = [13, 23]
        self.player.pix_pos = self.player.get_pixPos()
        self.player.direction *= 0
        self.enemy1.grid_pos = [11, 15]
        self.enemy1.pix_pos = self.enemy1.get_pixPos()
        self.enemy1.direction *= 0
        self.enemy2.grid_pos = [11, 13]
        self.enemy2.pix_pos = self.enemy2.get_pixPos()
        self.enemy2.direction *= 0
        self.enemy3.grid_pos = [16, 13]
        self.enemy3.pix_pos = self.enemy3.get_pixPos()
        self.enemy3.direction *= 0
        self.enemy4.grid_pos = [16, 15]
        self.enemy4.pix_pos = self.enemy4.get_pixPos()
        self.enemy4.direction *= 0
        with open("walls.txt", 'r') as file:
            for yIndex, line in enumerate(file):
                for xIndex, char in enumerate(line):
                    if char == "C":
                        self.coinsList.append(vec(xIndex, yIndex))
                    elif char == "E":
                        self.pelletsList.append(vec(xIndex, yIndex))

    def reset_2(self):
        self.coinsEaten = 'false'
        self.tim *=0
        self.l *= 0
        self.stateE1 = 'stop'
        self.stateE2 = 'stop'
        self.stateE3 = 'stop'
        self.stateE4 = 'stop'
        self.coinsList = []
        self.pelletsList = []
        self.player.grid_pos = [13, 23]
        self.player.pix_pos = self.player.get_pixPos()
        self.player.direction *= 0
        self.enemy1.grid_pos = [11, 15]
        self.enemy1.pix_pos = self.enemy1.get_pixPos()
        self.enemy1.direction *= 0
        self.enemy2.grid_pos = [11, 13]
        self.enemy2.pix_pos = self.enemy2.get_pixPos()
        self.enemy2.direction *= 0
        self.enemy3.grid_pos = [16, 13]
        self.enemy3.pix_pos = self.enemy3.get_pixPos()
        self.enemy3.direction *= 0
        self.enemy4.grid_pos = [16, 15]
        self.enemy4.pix_pos = self.enemy4.get_pixPos()
        self.enemy4.direction *= 0
        with open("walls.txt", 'r') as file:
            for yIndex, line in enumerate(file):
                for xIndex, char in enumerate(line):
                    if char == "C":
                        self.coinsList.append(vec(xIndex, yIndex))
                    elif char == "E":
                        self.pelletsList.append(vec(xIndex, yIndex))

    def delay(self):
        pygame.time.delay(500)
