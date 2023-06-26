import pygame
import psycopg2
from random import randint
import pygame_menu

pygame.init()

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="qwerty123"
)

cursor = connection.cursor()
# def create(): 
#     connection = psycopg2.connect(database = 'postgres', user = 'postgres', password = 'qwerty123') 
#     cur = connection.cursor() 
#     cur.execute( 
#         ''' 
#         CREATE TABLE snake_scores ( 
#             name VARCHAR(50), 
#             number VARCHAR(50) 
#         ); 
#         ''') 
#     connection.commit() 
#     cur.close() 
# create()
# cur = connection.cursor()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_COLOR = (50, 50, 50)
font = pygame.font.SysFont("Verdana", 20)

w = 500
ws = 700
h = 500
BLOCK_SIZE = 20
sc = pygame.display.set_mode((ws,h))
pygame.display.set_caption("Snake")
Clock = pygame.time.Clock()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Food:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.location = Point(self.x, self.y)
    
    def draw(self):
        point = self.location
        pygame.draw.rect(sc, (0,255,0),(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y,BLOCK_SIZE,BLOCK_SIZE))
    
    def respawn(self,dx,dy):
        self.dx = dx
        self.dy = dy
        self.location = Point(self.dx, self.dy)

class Speed:
    def __init__(self):
        self.x = randint(2, 22)
        self.y = randint(2, 22)
        self.location = Point(self.x, self.y)
    
    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(sc, (255, 255, 0), rect)

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = Point(self.x, self.y)
        
    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(sc, (0, 0, 255), rect)

class Snake:
    def __init__(self):
        self.body = [Point(10,11)]
        self.dx = 0
        self.dy = 0
    
    def move(self):
        for i in range(len(self.body)-1,0,-1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        
        self.body[0].x+=self.dx
        self.body[0].y+=self.dy

        if self.body[0].x*BLOCK_SIZE > w-1:
            self.body[0].x = 0
        
        if self.body[0].y*BLOCK_SIZE > h-1:
            self.body[0].y = 0
        
        if self.body[0].x < 0:
            self.body[0].x = w/BLOCK_SIZE-1

        if self.body[0].y < 0:
            self.body[0].y = h/BLOCK_SIZE-1

    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(sc, (255, 0, 0), rect)

        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(sc, (0, 255, 0), rect)

    def check_collision(self, food, block, speeds):
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                global SCORE, count, number
                count = 0
                number+=1
                SCORE+=randint(1, 3)
                self.body.append(Point(food.location.x, food.location.y))
                if food.location.x != block.x and food.location.y != block.y:
                    food.location.x, food.location.y = randint(2, 22), randint(2, 22)
        if self.body[0].x == speeds.location.x:
            if self.body[0].y == speeds.location.y:
                global LEVEL, FPS, level
                level+=1
                level%=2
                LEVEL+=1
                if speeds.location.x != block.x and speeds.location.y != block.y:
                    speeds.location.x, speeds.location.y = randint(2, 22), randint(2, 22)

def drawGrid():
    for x in range(0,w,BLOCK_SIZE):
        for y in range(0,h,BLOCK_SIZE):
            pygame.draw.rect(sc, LINE_COLOR, (x,y,BLOCK_SIZE,BLOCK_SIZE),1)

level = 0
LEVEL = 0
FPS=5
number = 0
count = 0
block = Block(0, 0)
snake = Snake()
food = Food(randint(1,25), randint(1,25))
speeds = Speed()
gameOver = False
gameStart = True
direction = 'RIGHT'
change_to = direction
save = False

def name_checker(NAMEBOX):
    global SCORE
    global user_name
    global cnt
    cnt = 0
    user_name = str(NAMEBOX.get_value())
    cursor.execute(' SELECT * FROM snake_scores ')
    data = cursor.fetchall()
    for row in data:
        if user_name == str(row[0]):
            cnt+=1

    if cnt==1:
        for row in data:
            SCORE = int(row[1])
            
    else:
        SCORE = 0
    start()

def start():
    gameStart = True
    global change_to
    global direction
    global number
    global SCORE
    global LEVEL
    global count
    global gameOver
    global level
    global FPS
    global save
    global user_name
    while gameStart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_UP :
                    change_to = 'UP'
                if event.key == pygame.K_DOWN :
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT :
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT :
                    change_to = 'RIGHT'
                # if event.key == pygame.K_RIGHT:
                #     snake.dx = 1
                #     snake.dy = 0
                # if event.key == pygame.K_LEFT:
                #     snake.dx = -1
                #     snake.dy = 0
                # if event.key == pygame.K_UP:
                #     snake.dx = 0
                #     snake.dy = -1
                # if event.key == pygame.K_DOWN:
                #     snake.dx = 0
                #     snake.dy = 1
                if event.key == pygame.K_i:
                    cursor.execute(f''' INSERT INTO snake_scores("name", "number") VALUES( '{user_name}', '{SCORE}'); ''')
                        
                    connection.commit()
                    cursor.close()
                    connection.close()
        if change_to == 'UP' and direction != 'DOWN' :
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP' :
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT' :
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT' :
            direction = 'RIGHT'


        if direction == 'UP' :
            snake.dx = 0
            snake.dy = -1
        if direction == 'DOWN' :
            snake.dx = 0
            snake.dy = 1
        if direction == 'LEFT' :
            snake.dx = -1
            snake.dy = 0
        if direction == 'RIGHT' :
            snake.dx = 1
            snake.dy = 0
        wallsDoor = open(f"level{level}.txt", 'r').readlines()
        walls = []
        for i,line in enumerate(wallsDoor):
            for j, each in enumerate(line):
                if each == '#':
                    walls.append(Block(j,i))
        drawGrid()
        for block in walls:
            block.draw()
            if snake.body[0].x == block.x and snake.body[0].y ==block.y:
                gameStart = False
                save = True
            for main in range(1,number):
                if snake.body[0].x == snake.body[main].x and snake.body[0].y == snake.body[main].y:
                    gameStart = False
                    save = True
            if food.x != block.x and food.y != block.y:
                food.draw()
            if SCORE >= 5 and level!=1:
                if speeds.x!=block.x and speeds.y!=block.y:
                    speeds.draw()
        
        snake.move()

        snake.check_collision(food,block,speeds)
        snake.draw()

        if SCORE > 1 and SCORE%5 == 0:
            LEVEL+=1
            FPS+=5

        count += (FPS % 3)
        if count%100==0 and count>0:
            food.respawn(randint(2,21), randint(2,21))

        score_img = font.render(f"{SCORE}", True, BLACK)
        coins_cnt = font.render(f"{LEVEL}", False, False)
        sc.blit(font.render(f"SCORE", True, BLACK), (565, 25))
        sc.blit(font.render("LEVEL", True, BLACK), (570, 135))
        sc.blit(score_img, score_img.get_rect(center=(600, 65)))
        sc.blit(coins_cnt, coins_cnt.get_rect(center=(600, 170)))
        if(save == True):
            global cnt
            data = cursor.fetchall()
            if cnt>=1:
                cursor.execute('UPDATE snake_scores set "number"=%s where "name"=%s',(SCORE,user_name))
                connection.commit()
                cursor.close()
                connection.close()
            else:
                cursor.execute(f'''INSERT INTO snake_scores("name", "number") VALUES( '{user_name}', '{SCORE}'); ''')
                connection.commit()
                cursor.close()
                connection.close()

        pygame.display.update()
        Clock.tick(FPS)
        sc.fill(WHITE)

menu = pygame_menu.Menu('Welcome', w, h,
                       theme=pygame_menu.themes.THEME_BLUE)
name_box = menu.add.text_input('Name :')
menu.add.button('Play', name_checker, name_box)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(sc)
pygame.quit()