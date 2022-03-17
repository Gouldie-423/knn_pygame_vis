import pygame
import random

#need to reuse for resets
def create_points():

    red_points = []
    blue_points = []

    for i in range(0,10):
        blue_x = random.randint(0,800)
        blue_y = random.randint(0,600)
        red_x = random.randint(200,600)
        red_y = random.randint(100,500)
        blue_points.append([blue_x,blue_y])
        red_points.append([red_x,red_y])

    return red_points,blue_points

def euclidean_distance(index,point_a,point_b):
    #point_a represents the randomly generated point
    #point_b represents the position of the mouse

    #x_diff and y_diff both calculate the square of the difference between the two points on the x and y axis
    x_diff = (point_a[index][0]-point_b[0])**2
    y_diff = (point_a[index][1]-point_b[1])**2

    #distance is finally calculated by taking the square root of the sum of differences of x and y axis
    distance = (x_diff+y_diff)**.5

    return distance

def sort_distances(red_points,blue_points,mouse):
    distances = [] 
    for i in range(0,len(blue_points)):
        blue_distance = euclidean_distance(i,blue_points,mouse)
        red_distance = euclidean_distance(i,red_points,mouse)
        
        #appending the 0 or 1 indicates the label used in the pick_color function
        distances.append([blue_distance,0])
        distances.append([red_distance,1])
    distances.sort()

    return distances

#need to adjust color dynamically per frame
def pick_color(distances,k):
        red = 0
        blue = 0
        for i in distances[:k]: #explicit for loop only pulling slice of smallest distances up to k indexes
            #below is conditional logic identifying which is the most prominent label
            if i[1] == 0:
                blue+=1
            if i[1] == 1:
                red+=1
        if red>blue:
            return coloring_red
        if red<blue:
            return coloring_blue

red_points,blue_points = create_points()

pygame.init()
clock=pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
color = (0,0,0)
drawing = True
coloring_blue = pygame.Color('deepskyblue')
coloring_red = pygame.Color('plum')
point_size = 15

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('KNN VIS')
game_display.fill(WHITE)

k = 3


while True: #updates game

    for event in pygame.event.get(): #checks for all user actions
        #pygame calls all user interactions events (click button, moving mouse, .etc)
        if event.type == pygame.QUIT: #checks if user clicks x at top of screen
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            #press r to change points & wipe screen
            if event.key == pygame.K_r:
                game_display.fill(WHITE)
                blue_points.clear()
                red_points.clear()
                red_points,blue_points = create_points()
    #getting mouse pos
    mouse = pygame.mouse.get_pos()
    
    #calculating distances for each point and labeling
    distances = sort_distances(red_points,blue_points,mouse)
    
    #displaying randomly generated points each frame
    for i in blue_points:
        point = pygame.Rect(i[0],i[1],point_size,point_size)
        pygame.draw.ellipse(game_display,BLUE,point)

    for i in red_points:
        point = pygame.Rect(i[0],i[1],point_size,point_size)
        pygame.draw.ellipse(game_display,RED,point)

    #drawing
    mouse_point = pygame.Rect(mouse[0],mouse[1],15,15)
    pygame.draw.ellipse(game_display,pick_color(distances,k),mouse_point)
    distances.clear()#need to refresh distances each frame

    pygame.display.flip() #entire purpose is to take everything in the loop and draw a picture from it
    clock.tick(60) # same clock we defined earlier. Limits how fast loop runs (60fps)

