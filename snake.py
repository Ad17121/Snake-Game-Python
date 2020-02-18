import pygame
import random

pygame.init()

#? Set screen dimensions
screenWidth = 510
screenHeight = 560

size = 10 #? Size of grid

#? Create window
window = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Snake")

#? Define colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkGreen = (2, 78, 0)

window.fill(black)

clock = pygame.time.Clock()

class snake:
    def __init__(self):
        self.segments= [(4,4),(3,4),(2,4)]
        self.direction = "right"

    def move(self,grid):      
        if self.direction == "up":
            
            temp = []
            for i,(x,y) in enumerate(snake.segments):
                if not y <= 0:
                    if i == 0:
                        temp.append((x,y-1))
                    else:
                        temp.append(snake.segments[i-1])
                else:
                    print("Up error")
                    running = False
                    gameOver()
                    break
                    
            snake.segments = temp
            
            
        elif self.direction == "down":
            temp = []
            for i,(x,y) in enumerate(snake.segments):
                if i == 0:
                    temp.append((x,y+1))
                else:
                    temp.append(snake.segments[i-1])
            snake.segments = temp
            

        elif self.direction == "right":     
            temp = []
            for i,(x,y) in enumerate(snake.segments):
                if i == 0:
                    temp.append((x+1,y))
                else:
                    temp.append(snake.segments[i-1])
            snake.segments = temp
            
            
        elif self.direction == "left":
            temp = []
            for i,(x,y) in enumerate(snake.segments):
                if not x <= 0:
                    if i == 0:
                        temp.append((x-1,y))
                    else:
                        temp.append(snake.segments[i-1])
                else:
                    print("Left error")
                    running = False
                    gameOver()
                    break
                    
            snake.segments = temp
            

        drawGrid(grid)
        
class food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.eaten = False

    def place(self):
        self.x = random.randint(0,size-1)
        self.y = random.randint(0,size-1)
        
def gameOver():
    global running
    print("GAME OVER")
    font1 = pygame.font.SysFont('comicsans', 200, True)
    text = font.render("GAME OVER",1,red)
    window.blit(text, (300,5))
    pygame.time.wait(2000)
    
    

#? Draw grid
def drawGrid(grid):
    global score
    global running

    window.fill(black)
    text = font.render("Score: " + str(score), 1, green)
    window.blit(text, (5, 5))

    width = 40
    height = 40
    margin = 10
    copy = grid
    grid = []

    for row in range(size):
        grid.append([])
        for column in range(size):
            grid[row].append(0)
    try:
        for x,y in snake.segments:
            grid[y][x] = 1
    except:
        print("Right or down error")
        running = False
        gameOver()
    
        
        

            
    grid[food.y][food.x] = 2
    for row in range(size):
        for column in range(size):
            color = white
            if grid[row][column] == 1:
                color = green
            elif grid[row][column] == 2:
                color = red
                
            pygame.draw.rect(window, color, ((0 + width * column)+margin*column+margin, 50 + (0 + height * row)+margin*row+margin, width, height))
    pygame.display.update()   
    return copy     
    
    
    
grid = []

for row in range(size):
    grid.append([])
    for column in range(size):
        grid[row].append(0)

font = pygame.font.SysFont('comicsans', 30, True)

#? Main loop
running = True
score = 0
snake = snake()
food = food()
food.place()
grid = drawGrid(grid)


while running:
    clock.tick(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and snake.direction != "down":
        snake.direction = "up"
        
    if keys[pygame.K_DOWN] and snake.direction != "up":
        snake.direction = "down"
        
    if keys[pygame.K_RIGHT] and snake.direction != "left":
        snake.direction = "right"
    
    if keys[pygame.K_LEFT] and snake.direction != "right":
        snake.direction = "left"
    
    if keys[pygame.K_SPACE]:
        pygame.time.delay(100)
        food.place()
        grid = drawGrid(grid)

    snake.move(grid)
    grid = drawGrid(grid)

   
    if snake.segments[0] == (food.x,food.y):
        score += 1
        print(len(snake.segments))
        food.place()
        snake.segments.append((10,10))
            
        
   

    try:
        if snake.segments[0] in snake.segments[1:]:
            print("collision error")
            running = False
            gameOver()
    except:
        print("collision error")
        running = False
        gameOver()

    

pygame.quit()