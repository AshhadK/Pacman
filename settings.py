from pygame.math import Vector2 as vec
import pygame

MAZE_WIDTH,MAZE_HEIGHT = 560,620
WIDTH,HEIGHT = 610,670
ROWS,COLS = 30,28
cell_width = MAZE_WIDTH//COLS
cell_height = MAZE_HEIGHT // ROWS
SPACE = 50
PLAYER_COLOUR = (255, 255, 0)
FPS = 60
RED = (255,0,0)
BLACK = (0,0,0)
GREY = (107,107,107)
ghostRed = (255,0,0)
ghostPink = (255, 184, 255)
ghostAqua = (0, 255, 255)
ghostOrange = (255, 184, 82)
PELLET_COLOR = (255,255,255)
WHITE = (255,255,255)
START_TEXT_SIZE = 100
START_FONT = 'arial black'
playerStartPos = vec(13,23)
ghostOrangeStartPos = vec(50,50)
x = (250, 365)