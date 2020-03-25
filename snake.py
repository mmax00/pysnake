import pygame
import random

pygame.init()
WIDTH= 600
HEIGHT=WIDTH
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PySnake")
font = pygame.font.Font('freesansbold.ttf',(WIDTH//10))
small_font = pygame.font.Font('freesansbold.ttf',(WIDTH//20))

class Snake_body(object):
    def __init__(self,x,y,width,height,moving_side):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moving_side = moving_side
    def draw_body(self):
        pygame.draw.rect(win, (0, 255, 0),(self.x, self.y, self.width, self.height))
    def draw_head(self):
        #draws the head and eyes of the snake based on the current moving direction
        pygame.draw.rect(win, (0, 200, 0), (self.x, self.y, self.width, self.height))
        if self.moving_side =='up':
            pygame.draw.circle(win,(255,255,255),(self.x+self.width//4,self.y+self.width//4),self.width//4)
            pygame.draw.circle(win, (0, 0, 0), (self.x + self.width // 4, self.y + self.width // 4),self.width // 8)
            pygame.draw.circle(win, (255, 255, 255), (self.x + self.width -self.width//4, self.y + self.width // 4),self.width // 4)
            pygame.draw.circle(win, (0, 0, 0), (self.x + self.width - self.width // 4, self.y + self.width // 4), self.width // 8)
        if self.moving_side == 'down':
            pygame.draw.circle(win, (255, 255, 255), (self.x + self.width // 4, self.y +  self.width - self.width // 4),self.width // 4)
            pygame.draw.circle(win, (0, 0, 0), (self.x + self.width // 4, self.y +  self.width - self.width // 4), self.width // 8)
            pygame.draw.circle(win, (255, 255, 255), (self.x + self.width - self.width // 4, self.y +  self.width - self.width // 4), self.width // 4)
            pygame.draw.circle(win, (0, 0, 0), (self.x + self.width - self.width // 4, self.y +  self.width - self.width // 4),self.width // 8)
        if self.moving_side =='left':
            pygame.draw.circle(win, (255, 255, 255), (self.x + self.width // 4, self.y +  self.width - self.width // 4),self.width // 4)
            pygame.draw.circle(win, (0, 0, 0), (self.x + self.width // 4, self.y +  self.width - self.width // 4), self.width // 8)
            pygame.draw.circle(win, (255, 255, 255),(self.x + self.width // 4, self.y +  self.width // 4),self.width // 4)
            pygame.draw.circle(win, (0, 0, 0), (self.x + self.width // 4, self.y +  self.width // 4),self.width // 8)
        if self.moving_side == 'right':
            pygame.draw.circle(win, (255, 255, 255), (self.x + self.width - self.width // 4, self.y + self.width // 4),self.width // 4)
            pygame.draw.circle(win, (0, 0, 0), (self.x + self.width - self.width // 4, self.y +self.width // 4), self.width // 8)
            pygame.draw.circle(win, (255, 255, 255), (self.x + self.width - self.width // 4, self.y +  self.width - self.width // 4), self.width // 4)
            pygame.draw.circle(win, (0, 0, 0), (self.x + self.width - self.width // 4, self.y +  self.width - self.width // 4),self.width // 8)
    def draw_tail(self):
        pygame.draw.rect(win, (0, 150, 0), (self.x, self.y, self.width, self.height))

def draw_background(screen_width,screen_height,rect_width,rect_height,spacing): #draws board background
    for i in range(0,int(screen_width/(rect_width+spacing))):
        for j in range(0,int(screen_height/(rect_height+spacing))):
            pygame.draw.rect(win,(255,255,255),(rect_width*i+i*spacing,j*rect_height+j*spacing,rect_width,rect_height))

def move_snake():
    global move_set
    move_set = False
    for i in range(len(snake)-1,-1,-1): #moves  the snake starting from tail to head
        if snake[i].moving_side == 'up':
            snake[i].y -= snake[i].height + spacing
        if snake[i].moving_side  == 'down':
            snake[i].y += snake[i].height + spacing
        if snake[i].moving_side  == 'left':
            snake[i].x -= snake[i].width + spacing
        if snake[i].moving_side  == 'right':
            snake[i].x += snake[i].width + spacing

        if i > 0 and snake[i - 1].moving_side != snake[i].moving_side: #If the direction of 'snake body' in front of isnt the same, changes it to
            snake[i].moving_side = snake[i - 1].moving_side


def draw_snake():
    for i in range(1, len(snake)):
        snake[i].draw_body()
        if i == len(snake)-1:
            snake[i].draw_tail()
    snake[0].draw_head()

def draw_apple(x,y,size):
    pygame.draw.rect(win,(255,0,0),(x,y,size,size))

def increase_snake(): #increases the size of the snake based on the moving direction
    if snake[len(snake)-1].moving_side == 'up':
        snake.append(Snake_body(snake[len(snake)-1].x,snake[len(snake)-1].y+(size+spacing),size,size,snake[len(snake)-1].moving_side))
    if snake[len(snake) - 1].moving_side == 'down':
        snake.append(Snake_body(snake[len(snake) - 1].x, snake[len(snake) - 1].y - (size+spacing), size, size,snake[len(snake) - 1].moving_side))
    if snake[len(snake) - 1].moving_side == 'left':
        snake.append(Snake_body(snake[len(snake) - 1].x+(size+spacing), snake[len(snake) - 1].y, size, size,snake[len(snake) - 1].moving_side))
    if snake[len(snake) - 1].moving_side == 'right':
        snake.append(Snake_body(snake[len(snake) - 1].x-(size+spacing), snake[len(snake) - 1].y, size, size,snake[len(snake) - 1].moving_side))
    draw_snake()

def check_collision():
    global playing,score,in_menu
    if snake[0].x == apple_x and  snake[0].y == apple_y:
        increase_snake()
        spawn_apple()
        score+=1
        if score==(WIDTH/(size+spacing))**2: #If the player won
            playing=False
            in_menu=True
    if snake[0].x >= WIDTH or snake[0].x<0 or snake[0].y<0 or snake [0].y>=HEIGHT:
        playing =False
        in_menu=True
    for i in range(1,len(snake)):
        if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
            playing=False
            in_menu=True


def spawn_apple():
    global apple_x,apple_y
    apple_x = random.randint(0,int(WIDTH/(size+spacing))-1)*(size+spacing)
    apple_y = random.randint(0, int(WIDTH / (size + spacing))-1) * (size + spacing)
    #Checks if spawned apple is on the snake
    for i in range(0,len(snake)):
        if apple_x==snake[i].x and apple_y == snake[i].y:
            spawn_apple()

def exit():
    #Exits game
    global playing,run,in_menu
    playing=False
    run =False
    in_menu = False
    pygame.quit()

def play_again():
    #Restart game
    global playing, run, in_menu,score
    playing = True
    in_menu = False
    score = 0
    spawn_apple()
    snake.clear()
    snake.append(Snake_body(size + spacing, size + spacing, size, size, 'down'))

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h))
        bt_text = small_font.render(msg, True, ic)

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(win, ic,(x,y,w,h))
        bt_text = small_font.render(msg, True, ac)

    textRect = bt_text.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(bt_text,textRect)

def draw_text(sc):
    go = font.render('PySnake', True, (0, 0, 0), (255, 255, 255))
    goRect = go.get_rect()
    goRect.center = (WIDTH // 2, HEIGHT // 2-HEIGHT//10)
    win.blit(go, goRect)
    if sc: #If its first time running it wont show score on the menu
        scr = small_font.render("Score: "+str(score),True, (0, 0, 0), (255, 255, 255))
        scrRect = scr.get_rect()
        scrRect.center = (WIDTH // 2, HEIGHT // 2-HEIGHT//40)
        win.blit(scr, scrRect)

size =39
spacing=1

snake = []
#Adds the head of the snake
snake.append(Snake_body(size+spacing,size+spacing,size,size,'down'))

apple_x=0
apple_y=0

spawn_apple()

score =1
#Speeds up the game
gamespeed_reducer = 50//(WIDTH/(size+spacing))

run = True
playing =False
in_menu=True
show_score=False
move_set = False
while run:
    while playing:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                playing=False
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_UP:
                    if len(snake)==1 or snake[0].moving_side!='down' and not move_set: #Checks if move is set so it doesnt glitch
                        snake[0].moving_side = 'up'
                        move_set=True
                if event.key ==pygame.K_DOWN :
                    if len(snake) == 1 or snake[0].moving_side != 'up'and not move_set:
                        snake[0].moving_side='down'
                        move_set=True
                if event.key == pygame.K_LEFT :
                    if len(snake) == 1 or snake[0].moving_side != 'right'and not move_set:
                        snake[0].moving_side='left'
                        move_set=True
                if event.key ==pygame.K_RIGHT :
                    if len(snake) == 1 or snake[0].moving_side != 'left' and not move_set:
                        snake[0].moving_side = 'right'
                        move_set=True

        win.fill((0, 0, 0))
        move_snake()
        check_collision()
        draw_background(WIDTH,HEIGHT,size,size,spacing)
        draw_apple(apple_x, apple_y, size)
        draw_snake()
        
        if not show_score:
            show_score = True

        pygame.display.update()
        pygame.time.delay(500-int(score*gamespeed_reducer))

    while in_menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                in_menu=False

        draw_background(WIDTH, HEIGHT, size, size, spacing)

        draw_text(show_score)

        btn_play = button("Play",WIDTH//2-WIDTH//20*3,WIDTH//2+WIDTH//20,WIDTH//20*6,WIDTH//20*2,(255,255,255),(0,0,0),play_again)
        btn_exit = button("Exit",WIDTH//2-WIDTH//20*3,(WIDTH//20)*4+WIDTH//2,WIDTH//20*6,WIDTH//20*2,(255,255,255),(0,0,0),exit)
        pygame.display.update()


pygame.quit()