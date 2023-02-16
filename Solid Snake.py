import pygame
import random
pygame.init()
fenetre=pygame.display.set_mode((1100,800))
pygame.display.set_caption("Metal Gear 4")
solidus = pygame.image.load("Resources/snake.png")
solidus = pygame.transform.scale(solidus,(50,50))
BGrnd = pygame.image.load("Resources/Background.png").convert()
BGrnd = pygame.transform.scale(BGrnd,(1100,800))
supply = pygame.image.load("Resources/supply.png")
supply = pygame.transform.scale(supply,(50,50))
carton = pygame.image.load("Resources/carton.png")
carton = pygame.transform.scale(carton,(50,50))
game_over=False
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0
clock = pygame.time.Clock()
solidus_speed=10
font_style = pygame.font.SysFont(None, 50)
pygame.mixer.init()
pygame.display.set_icon(pygame.image.load('Resources/snake.png'))
Menu=True
def score(score):
    value = font_style.render("Cartons: " + str(score), True, [255, 255, 255])
    fenetre.blit(value, [0, 0])
def metal_snake(snake_list):
    i = 0
    while i < len(snake_list):
        if i == len(snake_list)-1:
            fenetre.blit(solidus, [snake_list[i][0], snake_list[i][1],50,50])
        else:
            fenetre.blit(carton, [snake_list[i][0], snake_list[i][1],50,50])
        i += 1
def Defeat():
    msgl1 = font_style.render("Snake? Snake? ... SNAKE! vous avez perdu!", True, [0,0,0])
    msgl2 = font_style.render(" [esc] pour quiter [enter] pour rejouer",True,[0,0,0])
    fenetre.blit(msgl1, [50,800/2])
    fenetre.blit(msgl2, [50,1000/2])
def gameLoop():
    pygame.mixer.music.load("Resources/OST.mp3")
    pygame.mixer.music.play(loops = -1)
    game_over = False
    game_close = False
    x1 = 1100 / 2
    y1 = 800 / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    snake_Length = 1
    supplyx = round(random.randrange(0, 1100 - 50) / 50.0) * 50.0
    supplyy = round(random.randrange(0, 800 - 50) / 50.0) * 50.0
    while not game_over:
        while game_close == True:
            fenetre.blit( BGrnd,(0,0))
            Defeat()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_RETURN:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -50
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 50
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -50
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 50
                    x1_change = 0
        if x1 >= 1100 or x1 < 0 or y1 >= 800 or y1 < 0:
            pygame.mixer.Sound.play(pygame.mixer.Sound("Resources/death.mp3"))
            pygame.mixer.music.stop()
            game_close = True
        x1 += x1_change
        y1 += y1_change
        fenetre.blit( BGrnd,(0,0))
        fenetre.blit( supply, [supplyx, supplyy, 50, 50])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > snake_Length:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        metal_snake(snake_List)
        score(snake_Length - 1)
        pygame.display.update()
        if x1 == supplyx and y1 == supplyy:
            supplyx = round(random.randrange(0, 1100 - 50) / 50.0) * 50.0
            supplyy = round(random.randrange(0, 800 - 50) / 50.0) * 50.0
            snake_Length += 1
        clock.tick(solidus_speed)
    pygame.display.update()
    pygame.quit()
    quit()
while(Menu==True):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                gameLoop()
            if event.key == pygame.K_ESCAPE:
                quit()
    fenetre.blit( BGrnd,(0,0))
    msgl1 = font_style.render("Metal Gear 4: Snake misadventure", True, [200,0,0])
    msgl2 = font_style.render(" [esc] pour quiter [enter] pour jouer",True,[0,0,0])
    fenetre.blit(msgl1, [250,200/2])
    fenetre.blit(msgl2, [50,1000/2])
    pygame.display.update()