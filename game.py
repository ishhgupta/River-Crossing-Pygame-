import pygame as pg
import random
from config import*


pg.init()
pg.display.set_caption("Python game")

start_time = int(pg.time.get_ticks())//1000
win = pg.display.set_mode((win_width, win_height))

# declaring font types ###############################################3
bigfont = pg.font.Font(None, 80)
smallfont = pg.font.Font(None, 50)
mediumfont = pg.font.Font(None, 60)

######### loading images ######################################################
player1 = load_image('./img/starfish.png', 70, 70)
fix_ob = load_image("./img/alga.png", 80,
                    80), load_image("./img/coral.png", 80, 80)
mov_ob = load_image("./img/submarine.png", 70, 70)


####### function to determine winner ##############################
def winners(s1, s2):
    if s1 > s2:
        mssg = "PLAYER-A"
        win_score = s1
        text = mediumfont.render("winner = A score = " + str(s1),True, RED)
    if s2 > s1:
        mssg = "PLAYER-B"
        win_score = s2
        text = mediumfont.render("winner = A score = " + str(s2),True, RED)
    win.fill(BLUE)
    text = mediumfont.render(mssg + " wins with Score =  " + str(win_score) , True, RED)
    # text = mediumfont.render()
    text_rect = text.get_rect()
    text_x = win.get_width() / 2 - text_rect.width / 2
    text_y = win.get_height() / 2 - text_rect.height / 2
    win.blit(text, [text_x, text_y])


####### moving-obstacles class ####################################################
class Movobstacle(pg.sprite.Sprite):
    vel = 3

    def __init__(self, x, y):
        super(Movobstacle, self).__init__()
        self.x = x
        self.y = y
        self.surface = mov_ob

    def update(self, p):
        self.x += self.vel
        if(self.x > win_width):
            self.x = 0
        if collision(p.x1, p.y1, 70, 70, self.x, self.y, 70, 70):
            p.collided = True


# inserting obstacles
obs_list = []
mov_list = pg.sprite.Group()
pg.display.update()
for j in range(1, 5):
    for i in range(5):
        obs_list += [Obstacle(random.randint(0, 1000),
                              level[j], random.choice(fix_ob))]
for i in range(20):
    mov_list.add(Movobstacle(random.randint(
        0, 1000), random.choice(level)-110))


################mainLoop#####################################################
final_scoreA = 0
final_scoreB = 0
scoreA = 0
scoreB = 0
while loop:
    # scoreA = 0
    # scoreB = 0
    p1_check = 0
    p2_check = 0

    #### loop for player A ############################################
    p1 = Player(ini_x, ini_y)
    while run:
        pg.time.delay(50)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                loop = False

        # drawing elements
        win.fill((0, 0, 0))
        win.fill(BLUE)
        for i in range(6):
            pg.draw.rect(win, (0, 153, 0), (0, level[i], win_width, 70))

        start_text = smallfont.render("Start", True, (255, 255, 0))
        win.blit(start_text, (ini_x, ini_y))
        end_text = smallfont.render("End", True, (255, 255, 0))
        win.blit(end_text, (end_x, end_y))

        win.blit(player1, (p1.x1, p1.y1))
        keys = pg.key.get_pressed()
        p1.update(keys)
        for obs in obs_list:
            win.blit(obs.surface, (obs.x, obs.y))
            obs.update(p1)
        for obs in mov_list:
            win.blit(obs.surface, (obs.x, obs.y))
            obs.update(p1)

        # UPDATING SCORES
        if p1.y1 < 814 and p1_check == 0:
            scoreA += 10
            p1_check += 1
        if p1.y1 < 744 and p1_check == 1:
            scoreA += 5
            p1_check += 1
        if p1.y1 < 628 and p1_check == 2:
            scoreA += 10
            p1_check += 1
        if p1.y1 < 558 and p1_check == 3:
            scoreA += 5
            p1_check += 1
        if p1.y1 < 442 and p1_check == 4:
            scoreA += 10
            p1_check += 1
        if p1.y1 < 372 and p1_check == 5:
            scoreA += 5
            p1_check += 1
        if p1.y1 < 256 and p1_check == 6:
            scoreA += 10
            p1_check += 1
        if p1.y1 < 186 and p1_check == 7:
            scoreA += 5
            p1_check += 1
        if p1.y1 < 70 and p1_check == 8:
            scoreA += 10
            p1_check += 1

        # drawing scores related elements
        player_name = smallfont.render("Player-A", True, RED)
        win.blit(player_name, (0, 0))
        score_text = smallfont .render('ScoreA: ' + str(scoreA), 1, COLOR)
        win.blit(score_text, (0, 35))
        current_time = int(pg.time.get_ticks())//1000
        passed_time = current_time - start_time
        timer = smallfont .render('Timer: ' + str(passed_time), 1, COLOR)
        win.blit(timer, (0, 70))

        if p1.collided == True:
            start_time = current_time
            final_scoreA = scoreA - passed_time
            hold = True
            run = False
        if p1.x1 > end_x - 10 and p1.y1 < end_y + 10:
            start_time = current_time
            win1 = 1
            hold = True
            run = False

        pg.display.update()

    ##### loop for player B ########################################################
    p2 = Player(end_x, end_y)
    while hold:
        pg.time.delay(50)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                hold = False
                loop = False

        # drawing elements
        win.fill((0, 0, 0))
        win.fill(BLUE)
        for i in range(6):
            pg.draw.rect(win, (0, 153, 0), (0, level[i], win_width, 70))

        start_text = smallfont.render("End", True, (255, 255, 0))
        win.blit(start_text, (ini_x, ini_y))
        end_text = smallfont.render("Start", True, (255, 255, 0))
        win.blit(end_text, (end_x-15, end_y))

        win.blit(player1, (p2.x1, p2.y1))
        keys = pg.key.get_pressed()
        p2.update(keys)
        for obs in obs_list:
            win.blit(obs.surface, (obs.x, obs.y))
            obs.update(p2)
        for obs in mov_list:
            win.blit(obs.surface, (obs.x, obs.y))
            obs.update(p2)

        # UPDATING SCORES
        if p2.y1 > 186 and p2_check == 0:
            scoreB += 10
            p2_check += 1
        if p2.y1 > 256 and p2_check == 1:
            scoreB += 5
            p2_check += 1
        if p2.y1 > 372 and p2_check == 2:
            scoreB += 10
            p2_check += 1
        if p2.y1 > 442 and p2_check == 3:
            scoreB += 5
            p2_check += 1
        if p2.y1 > 558 and p2_check == 4:
            scoreB += 10
            p2_check += 1
        if p2.y1 > 628 and p2_check == 5:
            scoreB += 5
            p2_check += 1
        if p2.y1 > 744 and p2_check == 6:
            scoreB += 10
            p2_check += 1
        if p2.y1 > 814 and p2_check == 7:
            scoreB += 5
            p2_check += 1
        if p2.y1 > 930 and p2_check == 8:
            scoreB += 10
            p2_check += 1

        # inserting scores related elements
        player_name = smallfont.render("Player-B", True, RED)
        win.blit(player_name, (0, 0))
        score_text = smallfont.render('ScoreB: ' + str(scoreB), 1, COLOR)
        win.blit(score_text, (0, 35))
        current_time = int(pg.time.get_ticks())//1000
        passed_time = current_time - start_time
        timer = smallfont .render('Timer: ' + str(passed_time), 1, COLOR)
        win.blit(timer, (0, 70))

        if p2.collided == True:
            final_scoreB = scoreB - passed_time
            hold = False
            winners(final_scoreA, final_scoreB)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    loop = False

        if p2.x1 < ini_x + 10 and p2.y1 > ini_y - 10:
            win2 = 1
            if win1 == 1 and win2 == 1:
                Movobstacle.vel += 10
                start_time = current_time
                scoreA = 0
                scoreB = 0
                run = True
                hold = False
            else:
                winners(final_scoreA, final_scoreB)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        loop = False
        pg.display.update()

pg.quit()
