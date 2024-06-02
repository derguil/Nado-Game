import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("nado game")

clock = pygame.time.Clock()

background = pygame.image.load("C:/Users/jinji/OneDrive/desktop/pyg/background.png")

character = pygame.image.load("C:/Users/jinji/OneDrive/desktop/pyg/character.png")
chracter_size = character.get_rect().size
chracter_width = chracter_size[0]
chracter_height = chracter_size[1]
chracter_x_pos = screen_width/2 - (chracter_width/2)
chracter_y_pos = screen_height - chracter_height

to_X = 0
to_Y = 0

character_speed = 0.6

enemy = pygame.image.load("C:/Users/jinji/OneDrive/desktop/pyg/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width/2 - (enemy_width/2)
enemy_y_pos = (screen_height/2) - (enemy_height/2)

game_font = pygame.font.Font(None,40)

total_time = 10

start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(60)

    print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_X -= character_speed
                pass
            if event.key == pygame.K_RIGHT:
                to_X += character_speed
                pass
            if event.key == pygame.K_UP:
                to_Y -= character_speed
                pass
            if event.key == pygame.K_DOWN:
                to_Y += character_speed                
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_X = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_Y = 0

    chracter_x_pos += to_X * dt
    chracter_y_pos += to_Y * dt

    if chracter_x_pos < 0:
        chracter_x_pos = 0
    elif chracter_x_pos > screen_width - chracter_width:
        chracter_x_pos = screen_width - chracter_width
    if chracter_y_pos < 0:
        chracter_y_pos = 0
    elif chracter_y_pos > screen_height - chracter_height:
        chracter_y_pos = screen_height - chracter_height

    character_rect = character.get_rect()
    character_rect.left = chracter_x_pos
    character_rect.top = chracter_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background,(0,0))
    screen.blit(character,(chracter_x_pos,chracter_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255))
    screen.blit(timer,(10,10))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update()
    
pygame.time.delay(2000)

pygame.quit()