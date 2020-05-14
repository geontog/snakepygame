import pygame
import random
import math
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock() 

class snakebit(object):
    def __init__(self,row,col,width,height):
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.xvel = 0
        self.yvel = 0

    def draw(self, win, head):
        if head:
            pygame.draw.rect(win, (255,100,0), (self.row*25,self.col*25, self.width, self.height), 0)
        else:
            pygame.draw.rect(win, (255,0,0), (self.row*25, self.col*25, self.width, self.height), 0)
        

class snake(object):
    def __init__(self, snakebit):
        self.parts = [snakebit]
        self.dead = False
    def draw(self, win):
        for i in range(len(self.parts)):
            if i == 0:
                self.parts[i].draw(win, True)
            else:
                self.parts[i].draw(win, False)

class food(object):
    def __init__(self, row, col, width, height):
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def draw(self, win):  
        pygame.draw.rect(win, (255,255,255), (self.row*25,self.col*25,self.width,self.height), 0)


def redrawGameWindow():
    win.fill((0,0,0))
    s1.draw(win)
    f1.draw(win)
    if s1.dead:
        win.blit(text, (140,200))
        win.blit(text2, (100,250))
    pygame.display.update()

font = pygame.font.SysFont('comicsans', 75, True)
font2 = pygame.font.SysFont('comicsans', 35, True)
text = font.render('You died ', 1, (0,255,255))
text2 = font2.render('Press enter to play again', 1, (0,255,255))
sb1 = snakebit(10.0, 10.0, 25, 25)
s1 = snake(sb1)
f1 = food(random.randint(1,19), random.randint(1,19), 25, 25)
run = True 
while run:
    clock.tick(13) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    if s1.dead == False:
        i = len(s1.parts)-1
        while i > 0:
            s1.parts[i].row = s1.parts[i-1].row
            s1.parts[i].col = s1.parts[i-1].col
            i -= 1
        
        head = s1.parts[0]    
        
        head.row += head.xvel
        head.col += head.yvel
        for i in range(len(s1.parts)):
            if head.row == s1.parts[i].row and head.col == s1.parts[i].col and i > 1:
                s1.dead = True 
        if head.row > 19 or head.row < 0 or head.col < 0 or head.col > 19:
            s1.dead = True    

        if head.row == f1.row and head.col == f1.col:
            f1.row = random.randint(1,19)
            f1.col = random.randint(1,19)
            s1.parts.append(snakebit(s1.parts[len(s1.parts)-1].row, s1.parts[len(s1.parts)-1].col, 25, 25))

        if head.yvel == 0: 
            if keys[pygame.K_DOWN]:
                head.yvel = 1
                head.xvel = 0
            if keys[pygame.K_UP]:
                head.yvel = -1
                head.xvel = 0
        if head.xvel == 0:         
            if keys[pygame.K_LEFT]:
                head.xvel = -1
                head.yvel = 0
            if keys[pygame.K_RIGHT]:
                head.xvel = 1
                head.yvel = 0

    else:
        if keys[pygame.K_RETURN]:
            s1.parts = [snakebit(10.0, 10.0, 25, 25)]
            s1.dead = False
            f1.row = random.randint(1,19)
            f1.col = random.randint(1,19) 
            
    redrawGameWindow()

pygame.quit()
