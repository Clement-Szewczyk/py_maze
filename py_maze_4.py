import pygame
import random
import time
from  py_maze_gfx import *
# available on git : https://github.com/blenderlab/py_maze.git

"""
0 = path
1 = wall
"""


NBCELL = 20 #size of the square maze (width) 
maze = [] # contains the area
visited = [] # contains the visited spots
backtrack = 0
vue3D = False

def countn(x,y):
    '''
    Function to count free cells around the (x,y) one.
    '''
    n=0
    if x>0 and maze[x-1][y]>0   : n=n+1
    if x<NBCELL-1 and maze[x+1][y]>0 : n=n+1
    if y>0 and maze[x][y-1]>0 : n=n+1
    if y<NBCELL-1 and maze[x][y+1]>0 : n=n+1
    return n

def viderLaby():
    m=[]
     # generate a free array; filled of 1:   (walls) 
    for i in range(0,NBCELL):
        line=[]
        for j in range(0,NBCELL):
            line.append(1)     
        m.append(line)
    return m

def viderVisited():
    v=[]
    # generate an unvisited array; filled of 0:    
    for i in range(0,NBCELL):
        line=[]
        for j in range(0,NBCELL):
            line.append(0)
        v.append(line)
    return v
    
def preparerLaby():
    """
    Function to generate an empty field:
    - all places are walls
    - all places are unvisited
    - start & end are marked as SPOT
    """
    backtrack=0
    maze = viderLaby()
    visited = viderVisited()

    # send the 2 arrays : maze & visited 
    return(maze,visited)

def prochainesCase(x,y):
    """
    returns a collection of tuples (x,y) of available places to go
    """
    # if coordinates are in the field AND there is at least 3 cases free around next one :
    possibles = []
    if (x>1 and visited[x-1][y]==0 )  :
        if (countn(x-1,y)==3):possibles.append((x-1,y))
    if (y>1  and visited[x][y-1]==0) :
         if (countn(x,y-1)==3):possibles.append((x,y-1))
    if (y<NBCELL-1  and visited[x][y+1]==0) :
         if (countn(x,y+1)==3): possibles.append((x,y+1))
    if (x<NBCELL-1  and visited[x+1][y]==0) :
         if (countn(x+1,y)==3):possibles.append((x+1,y))
    random.shuffle(possibles)
    return (possibles)

def genererLaby(x,y): 
    """
    return True if a path is found
    return false if no path found 
    """
    global backtrack
    #we are on the last cell (EXIT ! yeaaah!) :
    if x==NBCELL-2 and y==NBCELL-2 :
         print("fini...")
         maze[x][y]=0
         return True
    # Stipulate that our position is part of the path.
    maze[x][y]=0
    visited[x][y]=1
    # find other possibles ways:
    listechoix = prochainesCase(x,y)

    # if no way out -> backtrack : position is not a path and return false.
    if len(listechoix)==0:
        maze[x][y]=1
        return False
    # for each choice...
    for choix in listechoix :
        afficherLaby(maze,x,y,iso=vue3D)
        #... try to find a way out :
        if genererLaby(choix[0],choix[1]):
            # if it is, adding our point.
            maze[choix[0]][choix[1]]=0
            return True
    afficherLaby(maze,x,y,iso=vue3D)
        
    # all the possible ways are wrong : return false...
    # and count backtracking
    backtrack = backtrack +1
    afficherTexte(maze,22,2,"Backtracking...")

    return False

    

def sortirLaby(x,y):
    global backtrack
    #we are on the last cell (EXIT ! yeaaah!) :
    if x==NBCELL-2 and y==NBCELL-2 :
         afficherLaby(maze,x,y,player=True,iso=vue3D)
         return True
    ## Some code to add here ! 

def algoLee(x,y):
    for i in range(NBCELL):
        for j in range(NBCELL):
            if maze[i][j]==0:
                afficherTexte(maze,i,j,"0",iso=vue3D,color=BLACK)


#main loop :
playing = True
maze,visited = preparerLaby()
if genererLaby(1,1):
    afficherTexte(maze,22,2,"Fini")


while playing:
    # manage events (keys....)
    # force all events to be processed : 
    pygame.event.pump()
    for event in pygame.event.get():
        # if a key is pressed :
        if event.type == pygame.KEYDOWN :
            # and the key is ESCAPE :
            if event.key == pygame.K_ESCAPE:
                pygame.quit() # close pygame
                raise SystemExit #for a system close
            # and if the key is G
            if event.key == pygame.K_g:
                maze,visited = preparerLaby()
                if genererLaby(1,1):
                    print ("FIni !")
            if event.key == pygame.K_l:
                visited = viderVisited()
                algoLee(1,1)

            if event.key == pygame.K_x:
                visited = viderVisited()
                if sortirLaby(1,1):
                    print ("Sorti !")
                else:
                    print ("pas de sortie....")

   
pygame.quit()