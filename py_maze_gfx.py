import pygame
import random
import time

"""
0 = path
1 = wall
2 = unknown
3 = spot (start/end)
"""


# some gfx :
img_grass=pygame.image.load("assets/grass.png")
img_grass=pygame.transform.scale(img_grass, (30,25))
img_sand=pygame.image.load("assets/sand.png")
img_sand=pygame.transform.scale(img_sand, (30,25))
img_spot=pygame.image.load("assets/spot.png")
img_spot=pygame.transform.scale(img_spot, (30,25))
img_back=pygame.image.load("assets/back.png")
img_back=pygame.transform.scale(img_back, (30,25))


# and a little tree 


img_tree1=pygame.image.load("assets/tree1.png")
img_tree1=pygame.transform.scale(img_tree1, (30,40))

img_player=pygame.image.load("assets/player.png")
img_player=pygame.transform.scale(img_player, (10,20))

WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
GRASS= (20,120,20)
PATH =  (200,200,100)
SPOTS = (200,0,0)
PLAYER = (100,200,20)

#Init the pygame engine 
pygame.init()
# Screen size :
size = [600,400]
# create a screen object :
screen = pygame.display.set_mode(size)
# important : the window's caption :
pygame.display.set_caption("Laby algo")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)


def afficherTexte(maze,x,y,texte,iso=False,color=WHITE):
    cellw = 400//len(maze)
    img = font.render(texte, True, color)
    if iso:
        screen.blit(img,(280+x*(cellw-6)-y*12,40+y*(cellw-14)+x*7))
    else:
        screen.blit(img,(x*cellw+cellw/3,y*cellw+cellw/6))
    pygame.display.flip()
    


def afficherLaby(maze,curx,cury,player=False,iso=False):
    """
    procedure to draw the maze on the screen (isometric view)
    curx & cury is coordinate of current point
    """
    screen.fill((0,0,0)) # Beware : the parameter is a tuple
    # size of a square on the screen : 
    NBCELL=len(maze)
    # define the cell Width :
    cellw = 400//NBCELL
    if iso:
        for j in range(0,NBCELL):
            for i in range(0,NBCELL):
                # choose the pictcdpure to draw : 
                if (maze[i][j]==1):
                    screen.blit(img_grass,(280+i*(cellw-6)-j*12,40+j*(cellw-14)+i*7))
                if (maze[i][j]==0):
                    screen.blit(img_sand,(280+i*(cellw-6)-j*12,40+j*(cellw-14)+i*7))
                if (i==NBCELL-2 and j==NBCELL-2) or (i==1 and j==1):
                    screen.blit(img_spot,(280+i*(cellw-6)-j*12,40+j*(cellw-14)+i*7))
                if curx==i and cury==j:
                    screen.blit(img_back,(280+curx*(cellw-6)-cury*12,40+cury*(cellw-14)+curx*7))
       
        if player:
            screen.blit(img_player,(290+curx*(cellw-6)-cury*12,25+cury*(cellw-14)+curx*7))
    if not iso:
        for j in range(0,NBCELL):
            for i in range(0,NBCELL):
                # choose the pictcdpure to draw :
                rect=pygame.Rect( i*cellw,j*cellw , cellw,cellw)
                
                if (maze[i][j]==1):
                    color=GRASS
                if (maze[i][j]==0):
                    color=PATH
                if (i==NBCELL-2 and j==NBCELL-2) or (i==1 and j==1):
                    color=SPOTS
                if curx==i and cury==j:
                    color=PLAYER
                pygame.draw.rect(screen,color,rect)
                
    # update the screen display :   
    pygame.display.flip()
    #some slow down procedure ...
    time.sleep( 0.01 )
    
    