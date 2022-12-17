import pygame
pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Tower Of Hanoi")
x1,x2,x3 = 140,160,180
run = True


def towerOfH(n, BEG, AUX, END):
    if n == 1:
        BEG = BEG + 300
    if n > 1:
        towerOfH(n - 1, BEG, END, AUX)

        print(f"Move disc {n} from {BEG} to {END}")
        towerOfH(n - 1, AUX, BEG, END)


n = 1

while(run):
    for i in range(200,10000,300):
        pygame.draw.rect(screen, (0, 255, 0), (i, 100, 20, 300))

    pygame.draw.rect(screen, (255,0,0), (0, 400, 1000, 20))
    pygame.draw.rect(screen, (255, 0, 0), (0, 400, 1000, 20))

    disc3 = pygame.draw.rect(screen, (0, 0, 255), (x1, 380, 140, 20))
    disc2 = pygame.draw.rect(screen, (0, 0, 255), (x2, 360, 100, 20))
    disc1 = pygame.draw.rect(screen, (0, 0, 255), (x3, 340, 60, 20))

    towerOfH(n, x1, x2, x3)
    x1 += 300
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


