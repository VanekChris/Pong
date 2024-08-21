from imports import *
pygame.init()
pygame.mixer.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
fps = 60
clock = pygame.time.Clock()
margin = 50
sfx = pygame.mixer.Sound("sound/pong.ogg")
p1_score = 0
p2_score = 0
winner = 0
game_over = False

select = SelectRect("white", width // 2, 240, 350, 60, 2)
pong_text = TextRect(width // 2, 100, "PONG", 80, "white")
one_player_text = TextRect(width // 2, 240, "One Player Game", 20, "white")
two_player_text = TextRect(width // 2, 300, "Two Player Game", 20, "white")
how_play_text = TextRect(width // 2, 360, "How To Play", 20, "white")
quit_text = TextRect(width // 2, 420, "Quit", 20, "white")

menu_sprites = pygame.sprite.Group()
menu_sprites.add(select, pong_text, one_player_text, two_player_text, how_play_text, quit_text)

p1_paddle = Paddle("white", 25, 300, 10, 50)
p2_paddle = Paddle("white", 775, 300, 10, 50)
ball = Ball("white", width // 2, height // 2, 8)
player_1_text = TextRect(125, 25, "Score: 0", 20, "white")
player_2_text = TextRect(675, 25, "Score: 0", 20, "white")
game_sprites = pygame.sprite.Group()
game_sprites.add(p1_paddle, p2_paddle, ball, player_1_text, player_2_text)

player_1_win_text = TextRect(width // 2, 150, "Player 1", 80, "white")
player_2_win_text = TextRect(width // 2, 150, "Player 2", 80, "white")
win_text = TextRect(width // 2, 250, "WINS", 80, "white")
play_text = TextRect(200, 375, "Play", 20, "white")
again_text = TextRect(200, 425, "Again", 20, "white")
menu_text = TextRect(400, 400, "Menu", 20, "white")
quit = TextRect(600, 400, "Quit", 20, "white")
end_select = SelectRect("white", 200, 400, 150, 100, 2)
end_menu = pygame.sprite.Group()
end_menu.add(play_text, again_text, menu_text, quit, end_select)
player_1_win_screen = pygame.sprite.Group()
player_1_win_screen.add(player_1_win_text, win_text)
player_2_win_screen = pygame.sprite.Group()
player_2_win_screen.add(player_2_win_text, win_text)

menu_select = SelectRect("white", 200, 420, 200, 60, 2)
one_player_how_to = TextRect(200, 100, "Player One keys", 20, "white")
two_player_how_to = TextRect(200, 240, "Player Two keys", 20, "white")
back_to_menu = TextRect(200, 420, "Menu", 20, "white")
quit_text = TextRect(600, 420, "Quit", 20, "white")
w_key = TextRect(550, 75, "W for up", 20, "white")
s_key = TextRect(550, 125, "S for down", 20, "white")
up_key = TextRect(550, 225, "↑ for up", 20, "white")
down_key = TextRect(550, 275, "↓ for down", 20, "white")
how_to_sprites = pygame.sprite.Group()
how_to_sprites.add(menu_select, one_player_how_to, two_player_how_to, back_to_menu, w_key, s_key, up_key, down_key, quit_text)

def board():
    screen.fill("black")
    pygame.draw.line(screen, "white", (0, margin), (width, margin))

def menu():
    pygame.display.set_caption("Menu")
    run = True
    
    while run:
        screen.fill("black")
        menu_sprites.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN] and select.rect.y == 210:
                select.rect.y = 270
                sfx.play()
            elif keys[pygame.K_UP] and select.rect.y == 270:
                select.rect.y = 210
                sfx.play()
            elif keys[pygame.K_DOWN] and select.rect.y == 270:
                select.rect.y = 330
                sfx.play()
            elif keys[pygame.K_UP] and select.rect.y == 330:
                select.rect.y = 270
                sfx.play()
            elif keys[pygame.K_DOWN] and select.rect.y == 330:
                select.rect.y = 390
                sfx.play()
            elif keys[pygame.K_UP] and select.rect.y == 390:
                select.rect.y = 330
                sfx.play()
            elif keys[pygame.K_DOWN] and select.rect.y == 390:
                select.rect.y = 210
                sfx.play()
            elif keys[pygame.K_UP] and select.rect.y == 210:
                select.rect.y = 390
                sfx.play()

            if keys[pygame.K_RETURN] and select.rect.y == 210:
                one_player_game()
            if keys[pygame.K_RETURN] and select.rect.y == 270:
                two_player_game()
            if keys[pygame.K_RETURN] and select.rect.y == 330:
                how_to_play()
                sfx.play()
            if keys[pygame.K_RETURN] and select.rect.y == 390:
                pygame.quit()
                sys.exit()
                run = False
        
        pygame.display.update()

def one_player_game():
    game_over = False
    p1_score = 0
    p2_score = 0
    
    pygame.time.delay(1500)
    run = True
    while run:
    
        clock.tick(fps)
        board()
        game_sprites.draw(screen)
        
        ball.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            p1_paddle.move(-20)
        if keys[pygame.K_s]:
            p1_paddle.move(20)

        if p2_paddle.rect.centery < ball.rect.top and p2_paddle.rect.bottom < 600:
            p2_paddle.rect.move_ip(0, 6.5)
        if p2_paddle.rect.centery > ball.rect.bottom and p2_paddle.rect.top > 50:
            p2_paddle.rect.move_ip(0, -6.5)

        if ball.rect.left <= 0:
            p2_score += 1
            ball.reset("white", width // 2, height // 2, 8)
            sfx.play()
        elif ball.rect.right >= width:
            p1_score += 1
            ball.reset("white", width // 2, height // 2, 8)
            sfx.play()
        if pygame.sprite.collide_rect(ball, p1_paddle) or pygame.sprite.collide_rect(ball, p2_paddle):
            ball.velocity[0] = -ball.velocity[0]
            sfx.play()
        
        if p1_score == 7 or p2_score == 7:
            game_over = True
            ball.velocity = [0, 0]

        if game_over:
            end_menu.draw(screen)
            if p1_score == 7:
                player_1_win_screen.draw(screen)
            elif p2_score == 7:
                player_2_win_screen.draw(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

            if game_over:
                if end_select.rect.x == 125 and keys[pygame.K_LEFT]:
                    end_select.rect.x = 525
                    sfx.play()
                elif end_select.rect.x == 525 and keys[pygame.K_RIGHT]:
                    end_select.rect.x = 125
                    sfx.play()
                elif end_select.rect.x == 525 and keys[pygame.K_LEFT]:
                    end_select.rect.x = 325
                    sfx.play()
                elif end_select.rect.x == 125 and keys[pygame.K_RIGHT]:
                    end_select.rect.x = 325
                    sfx.play()
                elif end_select.rect.x == 325 and keys[pygame.K_LEFT]:
                    end_select.rect.x = 125
                    sfx.play()
                elif end_select.rect.x == 325 and keys[pygame.K_RIGHT]:
                    end_select.rect.x = 525
                    sfx.play()

        if end_select.rect.x == 125 and keys[pygame.K_RETURN]:
            game_over = False
            p1_score = 0
            p2_score = 0
            ball.velocity = [7 * ball.direction, 7]
            one_player_game()
        if end_select.rect.x == 325 and keys[pygame.K_RETURN]:
            menu()
        if end_select.rect.x == 525 and keys[pygame.K_RETURN]:
            pygame.quit()
            sys.exit()
            run = False
        
        player_1_text.update(p1_score)
        player_2_text.update(p2_score)
        pygame.display.update()

def two_player_game():
    
    p1_score = 0
    p2_score = 0
    pygame.time.delay(1500)
    game_over = False
    run = True
    while run:
    
        clock.tick(fps)
        board()
        game_sprites.draw(screen)
        ball.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            p1_paddle.move(-5)
        if keys[pygame.K_s]:
            p1_paddle.move(5)
        if keys[pygame.K_UP]:
            p2_paddle.move(-5)
        if keys[pygame.K_DOWN]:
            p2_paddle.move(5)

        if ball.rect.left <= 0:
            p2_score += 1
            ball.reset("white", width // 2, height // 2, 8)
            sfx.play()
        elif ball.rect.right >= width:
            p1_score += 1
            ball.reset("white", width // 2, height // 2, 8)
            sfx.play()
        if pygame.sprite.collide_rect(ball, p1_paddle) or pygame.sprite.collide_rect(ball, p2_paddle):
            ball.velocity[0] = -ball.velocity[0]
            sfx.play()

        if p1_score == 7 or p2_score == 7:
            game_over = True
            ball.velocity = [0, 0]

        if game_over:
            end_menu.draw(screen)
            if p1_score == 7:
                player_1_win_screen.draw(screen)
            elif p2_score == 7:
                player_2_win_screen.draw(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

            if game_over:
                if end_select.rect.x == 125 and keys[pygame.K_LEFT]:
                    end_select.rect.x = 525
                    sfx.play()
                elif end_select.rect.x == 525 and keys[pygame.K_RIGHT]:
                    end_select.rect.x = 125
                    sfx.play()
                elif end_select.rect.x == 525 and keys[pygame.K_LEFT]:
                    end_select.rect.x = 325
                    sfx.play()
                elif end_select.rect.x == 125 and keys[pygame.K_RIGHT]:
                    end_select.rect.x = 325
                    sfx.play()
                elif end_select.rect.x == 325 and keys[pygame.K_LEFT]:
                    end_select.rect.x = 125
                    sfx.play()
                elif end_select.rect.x == 325 and keys[pygame.K_RIGHT]:
                    end_select.rect.x = 525
                    sfx.play()

        if end_select.rect.x == 125 and keys[pygame.K_RETURN]:
            game_over = False
            p1_score = 0
            p2_score = 0
            ball.velocity = [7 * ball.direction, 7]
            two_player_game()
        if end_select.rect.x == 325 and keys[pygame.K_RETURN]:
            menu()
        if end_select.rect.x == 525 and keys[pygame.K_RETURN]:
            pygame.quit()
            sys.exit()
            run = False
                
        player_1_text.update(p1_score)
        player_2_text.update(p2_score)
        pygame.display.update()

def how_to_play():
    pygame.display.set_caption("How To Play")
    run = True
    
    while run:
        screen.fill("black")
        how_to_sprites.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and menu_select.rect.x == 100:
                menu_select.rect.x = 500
                sfx.play()
            elif keys[pygame.K_LEFT] and menu_select.rect.x == 500:
                menu_select.rect.x = 100
                sfx.play()
            elif keys[pygame.K_RIGHT] and menu_select.rect.x == 500:
                menu_select.rect.x = 100
                sfx.play()
            elif keys[pygame.K_LEFT] and menu_select.rect.x == 100:
                menu_select.rect.x = 500
                sfx.play()

            if keys[pygame.K_RETURN] and menu_select.rect.x == 100:
                menu()
            if keys[pygame.K_RETURN] and menu_select.rect.x == 500:
                pygame.quit()
                sys.exit()
                run = False
        
        pygame.display.update()

menu()
one_player_game()
two_player_game()
pygame.quit()
sys.exit()