import pygame
import constance as c
from background import BG1, BG2, BG3, BG4
from ship import Ship
from bg_spawner import P1BgSpawner, P2BgSpawner, P3BgSpawner, P4BgSpawner
from enemy_spawner import EnemySpawner
from p2enemy_spawner import p2EnemySpawner
from p3enemy_spawner import p3EnemySpawner
from particle_spawner import ParticleSpawner
from explosion_spawner import ExplosionSpawner



pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
pygame.font.init()
##pygame.mixer.music.load("theme_music.ogg")
##pygame.mixer.music.set_volume(.5)
##pygame.mixer.music.play(loops=True)
fw = open('data.txt', 'w')
fw_stream = open('stream.txt', 'w')
fw_seconds = open('seconds.txt', 'w')




## if player.rect.x >= enemy_group1.rect.x:
    ##player.rect.x *<1 - so if player was to right of enemy, he bounces right


phase = 2
trial_type = 0
trial_num = 1
session = 1
tg_1 = 0
alt_1 = 0
score = 0
asteroids = 0







def main():
    global phase
    global trial_type
    global trial_num
    global session
    global tg_1
    global alt_1
    global score
    global asteroids
    run = True
    fps = 60
    clock = pygame.time.Clock()
    clock1 = pygame.time.Clock()
    delta_time = clock1.tick(60) / 1000
    level = 0
    display = pygame.display.set_mode(c.display_size)
    black = (0, 0, 0)
    display.fill(black)
    trial_timer = 7200
    phase_timer = 36000
    long_sdelta_timer = 18000
    long_sd1_timer = 9000
    long_sd2_timer = 9000
    short_sdelta_timer = 3600
    short_sd_timer = 3600
    shorter_sdelta_timer = 1800
    shorter_sd_timer = 1800
    thinning_step = 1
    time_count = 0
    seconds_count = 0
    stream = []
    number_shots = []
    seconds_timer = 60










    player = Ship()
    sprite_group = pygame.sprite.Group()
    sprite_group.add(player)
    ##shield_spawner = ShieldSpawner()
    particle_spawner = ParticleSpawner()
    p2enemy_spawner = p2EnemySpawner()
    enemy_spawner = EnemySpawner()
    p3enemy_spawner = p3EnemySpawner()
    explosion_spawner = ExplosionSpawner()
    p1bg_spawner = P1BgSpawner()
    p2bg_spawner = P2BgSpawner()
    p3bg_spawner = P3BgSpawner()
    p4bg_spawner = P4BgSpawner()





    def record_data():
        global alt_1
        global tg_1
        global session
        global phase
        global asteroids
        global score
        global trial_type
        global trial_num

        fw.write('\n')
        fw.write('phase = ')
        if phase == 1:
            fw.write('Baseline')
            fw.write('\n')
        elif phase == 2:
            fw.write('Treatment')
            fw.write('\n')
        elif phase == 3:
            fw.write('Extinction')
            fw.write('\n')
        fw.write('trial = ')
        fw.write(str(trial_num))
        fw.write('\n')
        fw.write('\n')
        fw.write('target = ')
        fw.write('\n')
        fw.write(str(tg_1))
        fw.write('\n')
        if phase >= 2:
            fw.write('alternative = ')
            fw.write('\n')
            fw.write(str(alt_1))
            fw.write('\n')
        fw.write('asteroids hit =')
        fw.write('\n')
        fw.write(str(asteroids))
        fw.write('\n')
        fw.write('score = ')
        fw.write('\n')
        fw.write(str(score))
        fw.write('\n')

        alt_1 = 0
        tg_1 = 0
        asteroids = 0



    def update_stream():
        nonlocal seconds_count
        nonlocal stream
        nonlocal number_shots
        fw_stream.write(str(seconds_count))
        fw_stream.write(str(stream))
        fw_stream.write('\n')
        stream = []


    def update_groups():
        sprite_group.update()
        particle_spawner.update()
        explosion_spawner.update()

        ##shield_spawner.update()

        if phase == 1:
            p1bg_spawner.update()
            enemy_spawner.update()
        if phase == 2:
            p2bg_spawner.update()
            p2enemy_spawner.update()
        if phase == 3:
            p4bg_spawner.update()
            p3enemy_spawner.update()
        if phase == 4:
            game_over()



    def update_display():
        particle_spawner.particle_group.draw(display)
        player.hud_group.draw(display)
        player.hud.score_group.draw(display)
        player.hud.asteroid_score_group.draw(display)
        sprite_group.draw(display)
        explosion_spawner.p1asteroidexplosions_group.draw(display)
        explosion_spawner.p2asteroidexplosions_group.draw(display)
        explosion_spawner.sdasteroidexplosions_group.draw(display)
        explosion_spawner.sdeltaasteroidexplosions_group.draw(display)
        explosion_spawner.shipexplosions_group.draw(display)
        ##shield_spawner.shipshield_group.draw(display)
        player.lasers.draw(display)
        player.lmuzzle_group.draw(display)
        player.rmuzzle_group.draw(display)
        player.engine_group.draw(display)
        player.ShipShield_group.draw(display)
        pygame.display.update()


        if phase == 1:
            p1bg_spawner.bg_group.draw(display) ## draws background with stars
            p1bg_spawner.stars_group.draw(display)
            enemy_spawner.enemy_group1.draw(display)
            enemy_spawner.powerups_group.draw(display)
            global enemy
            for enemy in enemy_spawner.enemy_group1:
                enemy.engine_group.draw(display)
                enemy.ShipShield_group.draw(display)
            enemy_spawner.asteroid_group.draw(display)
        if phase == 2:
            p2bg_spawner.bg_group.draw(display)
            p2enemy_spawner.enemy_group1.draw(display)
            for enemy in p2enemy_spawner.enemy_group1:
                enemy.engine_group.draw(display)
                enemy.ShipShield_group.draw(display)
            p2enemy_spawner.enemy_group2.draw(display)
            for enemy in p2enemy_spawner.enemy_group2:
                enemy.engine_group.draw(display)
                enemy.ShipShield_group.draw(display)
            p2enemy_spawner.p2asteroid_group.draw(display)
            p2enemy_spawner.powerups_group.draw(display)
        if phase == 3:
            p4bg_spawner.bg_group.draw(display)
            p3enemy_spawner.enemy_group1.draw(display)
            for enemy in p3enemy_spawner.enemy_group1:
                enemy.engine_group.draw(display)
                enemy.ShipShield_group.draw(display)
            p3enemy_spawner.enemy_group2.draw(display)
            for enemy in p3enemy_spawner.enemy_group2:
                enemy.engine_group.draw(display)
                enemy.ShipShield_group.draw(display)
            p3enemy_spawner.powerups_group.draw(display)
            p3enemy_spawner.sdeltaasteroid_group.draw(display)
        if phase == 4:
            game_over()


    while run:
        update_groups()
        update_display()
        time_count += 1
        clock.tick(fps)
        seconds_timer -= 1
        if seconds_timer == 0:
            seconds_count += 1
            update_stream()
            seconds_timer = 60
            if seconds_count == 600:
                seconds_count = 0
        if seconds_count == 120:
            record_data()
            if trial_num == 3:
                player.hud.asteroid_score.value = 0
                player.hud.asteroid_score.update_score(0)
                phase = 2
            elif trial_num == 6:
                player.hud.asteroid_score.value = 0
                player.hud.asteroid_score.update_score(0)
                phase = 3
            elif trial_num == 9:
                phase = 4
            trial_num += 1
            seconds_count = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.vel_x = -player.speed
                    player.turning_left = True
                    player.anim_index = 0
                    player.rev_engine()
                    ##player.ShipShield_group.vel_x = -shields.speed
                elif event.key == pygame.K_d:
                    player.vel_x = player.speed
                    player.turning_right = True
                    player.anim_index = 0
                    player.rev_engine()
                    ##player.ShipShield_group.vel_x = shields.speed
                elif event.key == pygame.K_w:
                    player.vel_y = -player.speed
                    player.rev_engine()
                    ##player.ShipShield_group.vel_y = -shields.speed
                elif event.key == pygame.K_s:
                    player.vel_y = player.speed
                    player.rev_engine()
                    ##player.ShipShield_group.vel_y = shields.speed
                if event.key == pygame.K_SPACE:
                    player.shoot()
                    stream.append(9)
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot()
                stream.append(9)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.vel_x = 0
                    player.go_straight()
                    player.turning_left = False
                    player.engine_die()
                    ##shields.vel_x = 0
                elif event.key == pygame.K_d:
                    player.vel_x = 0
                    player.go_straight()
                    player.turning_right = False
                    player.engine_die()
                    ##shields.vel_x = 0
                elif event.key == pygame.K_s:
                    player.vel_y = 0
                    player.engine_die()
                    ##shields.vel_y = 0
                elif event.key == pygame.K_w:
                    player.vel_y = 0
                    player.engine_die()
                    ##shields.vel_x = 0
        if phase == 1:
            collided = pygame.sprite.groupcollide(player.lasers, enemy_spawner.enemy_group1, True, False)
            for laser, enemy in collided.items():
                if enemy[0].is_invincible:
                    particle_spawner.spawn_particles((laser.rect.x, laser.rect.y))
                    tg_1 += 1
                    stream.append(1)
                    enemy[0].get_hit()
                elif not enemy[0].is_invincible:
                    enemy[0].get_hit()
                    player.hud.score.update_score(enemy[0].point_value)
                    score += 5
                    stream.append(8)

            collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.asteroid_group, False, True)  ## seperate badguy1 as alt1 group
            for player, new_asteroid in collided.items():
                ##shield_spawner.spawn_shipshield((player.rect.x, player.rect.y))
                new_asteroid[0].get_hit()

                if new_asteroid[0].is_destroyed:
                    asteroids += 1
                    player.hud.asteroid_score.update_score(new_asteroid[0].point_value)
                    stream.append(5)
                    explosion_spawner.spawn_p1asteroidexplosions((new_asteroid[0].rect.x, new_asteroid[0].rect.y))

            collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group1, False,
                                                  False)  ## seperate badguy1 as alt1 group
            for player, enemy in collided.items():
                player.start_shields()
                if player.rect.y > enemy[0].rect.y:
                    player.rect.y += 100
                    player.vel_y = 0
                elif player.rect.y < enemy[0].rect.y:
                    player.rect.y -= 100
                    player.vel_y = 0
                if player.rect.x > enemy[0].rect.x:
                    player.rect.x += 100
                    player.vel_x = 0
                if player.rect.x < enemy[0].rect.x:
                    player.rect.x -= 100
                    player.vel_x = 0

            collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.powerups_group, False, True)
            for player, powerup in collided.items():
                player.turning_left = False
                player.turning_right = False
                player.spinning = True


            collided = pygame.sprite.groupcollide(enemy_spawner.enemy_group1, enemy_spawner.asteroid_group, False, True)  ## seperate badguy1 as alt1 group
            for enemy, asteroid in collided.items():
                ##shield_spawner.spawn_shipshield((player.rect.x, player.rect.y))
                asteroid[0].get_hit()

                if asteroid[0].is_destroyed:
                    explosion_spawner.spawn_p1asteroidexplosions((asteroid[0].rect.x, asteroid[0].rect.y))
            for enemy in collided.items():
                enemy[0].new_shield()


        elif phase == 2:
            collided = pygame.sprite.groupcollide(player.lasers, p2enemy_spawner.enemy_group1, True, False)
            for laser, enemy in collided.items():
                if enemy[0].is_invincible:
                    ##particle_spawner.spawn_particles((laser.rect.x, laser.rect.y))
                    tg_1 += 1
                    stream.append(1)
                    enemy[0].get_hit()
                elif not enemy[0].is_invincible:
                    enemy[0].get_hit()
                    player.hud.score.update_score(enemy[0].point_value)
                    score += 5
                    stream.append(8)
            ##hits = pygame.sprite.spritecollide(sprite_group, p2enemy_spawner.asteroid_group, False, pygame.sprite.collide_circle)

            collided = pygame.sprite.groupcollide(sprite_group, p2enemy_spawner.enemy_group1, False,
                                                  False)  ## seperate badguy1 as alt1 group
            for player, enemy in collided.items():
                player.start_shields()
                if player.rect.y > enemy[0].rect.y:
                    player.rect.y += 100
                    player.vel_y = 0
                elif player.rect.y < enemy[0].rect.y:
                    player.rect.y -= 100
                    player.vel_y = 0
                if player.rect.x > enemy[0].rect.x:
                    player.rect.x += 100
                    player.vel_x = 0
                if player.rect.x < enemy[0].rect.x:
                    player.rect.x -= 100
                    player.vel_x = 0


            collided = pygame.sprite.groupcollide(sprite_group, p2enemy_spawner.powerups_group, False, True)
            for player, powerup in collided.items():
                player.turning_left = False
                player.turning_right = False
                player.spinning = True

            collided = pygame.sprite.groupcollide(sprite_group, p2enemy_spawner.enemy_group2, False,
                                                  False)  ## seperate badguy1 as alt1 group
            for player, enemy in collided.items():
                player.start_shields()
                if player.rect.y > enemy[0].rect.y:
                    player.rect.y += 100
                    player.vel_y = 0
                elif player.rect.y < enemy[0].rect.y:
                    player.rect.y -= 100
                    player.vel_y = 0
                if player.rect.x > enemy[0].rect.x:
                    player.rect.x += 100
                    player.vel_x = 0
                if player.rect.x < enemy[0].rect.x:
                    player.rect.x -= 100
                    player.vel_x = 0

            collided = pygame.sprite.groupcollide(sprite_group, p2enemy_spawner.p2asteroid_group, False, True)  ## seperate badguy1 as alt1 group
            for player, asteroid in collided.items():
                ##shield_spawner.spawn_shipshield((player.rect.x, player.rect.y))

                asteroid[0].get_hit()

                if asteroid[0].is_destroyed:
                    asteroids += 1
                    stream.append(5)
                    explosion_spawner.spawn_p1asteroidexplosions((asteroid[0].rect.x, asteroid[0].rect.y))
                    player.hud.asteroid_score.update_score(asteroid[0].point_value)

            collided = pygame.sprite.groupcollide(p2enemy_spawner.enemy_group1, p2enemy_spawner.p2asteroid_group, False, True)  ## seperate badguy1 as alt1 group
            for enemy, asteroid in collided.items():
                ##shield_spawner.spawn_shipshield((player.rect.x, player.rect.y))
                asteroid[0].get_hit()

                if asteroid[0].is_destroyed:
                    explosion_spawner.spawn_p1asteroidexplosions((asteroid[0].rect.x, asteroid[0].rect.y))
            for enemy in collided.items():
                enemy[0].new_shield()

            collided = pygame.sprite.groupcollide(p2enemy_spawner.enemy_group2, p2enemy_spawner.p2asteroid_group, False, True)  ## seperate badguy1 as alt1 group
            for enemy, asteroid in collided.items():
                ##shield_spawner.spawn_shipshield((player.rect.x, player.rect.y))
                asteroid[0].get_hit()
                if asteroid[0].is_destroyed:
                    explosion_spawner.spawn_p1asteroidexplosions((asteroid[0].rect.x, asteroid[0].rect.y))
            for enemy in collided.items():
                enemy[0].new_shield()


            collided = pygame.sprite.groupcollide(player.lasers, p2enemy_spawner.enemy_group2, True, False)
            for laser, enemy in collided.items():
                if enemy[0].is_invincible:
                    particle_spawner.spawn_particles((laser.rect.x, laser.rect.y))
                    alt_1 += 1
                    stream.append(2)
                    enemy[0].get_hit()
                elif not enemy[0].is_invincible:
                    enemy[0].get_hit()
                    player.hud.score.update_score(enemy[0].point_value)
                    score += 5
                    stream.append(8)

        elif phase == 3:
            collided = pygame.sprite.groupcollide(player.lasers, p3enemy_spawner.enemy_group1, True, False)
            for laser, enemy in collided.items():
                enemy[0].get_hit()
                ##particle_spawner.spawn_particles((laser.rect.x, laser.rect.y))
                tg_1 += 1
                stream.append(1)
                enemy[0].get_hit()
                if not enemy[0].is_invincible:
                    enemy[0].get_hit()

            collided = pygame.sprite.groupcollide(sprite_group, p3enemy_spawner.enemy_group1, False,
                                                  False)  ## seperate badguy1 as alt1 group
            for player, enemy in collided.items():
                player.start_shields()
                if player.rect.y > enemy[0].rect.y:
                    player.rect.y += 100
                    player.vel_y = 0
                elif player.rect.y < enemy[0].rect.y:
                    player.rect.y -= 100
                    player.vel_y = 0
                if player.rect.x > enemy[0].rect.x:
                    player.rect.x += 100
                    player.vel_x = 0
                if player.rect.x < enemy[0].rect.x:
                    player.rect.x -= 100
                    player.vel_x = 0

            collided = pygame.sprite.groupcollide(sprite_group, p3enemy_spawner.powerups_group, False, True)
            for player, powerup in collided.items():
                player.turning_left = False
                player.turning_right = False
                player.spinning = True

            collided = pygame.sprite.groupcollide(sprite_group, p3enemy_spawner.enemy_group2, False,
                                                  False)  ## seperate badguy1 as alt1 group
            for player, enemy in collided.items():
                player.start_shields()
                if player.rect.y > enemy[0].rect.y:
                    player.rect.y += 100
                    player.vel_y = 0
                elif player.rect.y < enemy[0].rect.y:
                    player.rect.y -= 100
                    player.vel_y = 0
                if player.rect.x > enemy[0].rect.x:
                    player.rect.x += 100
                    player.vel_x = 0
                if player.rect.x < enemy[0].rect.x:
                    player.rect.x -= 100
                    player.vel_x = 0

            collided = pygame.sprite.groupcollide(sprite_group, p3enemy_spawner.sdeltaasteroid_group, False, True)  ## seperate badguy1 as alt1 group
            for player, new_asteroid in collided.items():
                ##shield_spawner.spawn_shipshield((player.rect.x, player.rect.y)
                new_asteroid[0].get_hit()
                if new_asteroid[0].is_destroyed:
                    asteroids += 1
                    stream.append(5)
                    explosion_spawner.spawn_p1asteroidexplosions((new_asteroid[0].rect.x, new_asteroid[0].rect.y))
                    player.hud.asteroid_score.update_score(new_asteroid[0].point_value)

            collided = pygame.sprite.groupcollide(player.lasers, p3enemy_spawner.enemy_group2, True, False)
            for laser, enemy in collided.items():
                enemy[0].get_hit()
                ##particle_spawner.spawn_particles((laser.rect.x, laser.rect.y))
                alt_1 += 1
                stream.append(2)
                enemy[0].get_hit()
                if not enemy[0].is_invincible:
                    enemy[0].get_hit()

            collided = pygame.sprite.groupcollide(p3enemy_spawner.enemy_group1, p3enemy_spawner.sdeltaasteroid_group, False,
                                                  True)  ## seperate badguy1 as alt1 group
            for enemy, asteroid in collided.items():
                ##shield_spawner.spawn_shipshield((player.rect.x, player.rect.y))
                asteroid[0].get_hit()
                if asteroid[0].is_destroyed:
                    explosion_spawner.spawn_p1asteroidexplosions((asteroid[0].rect.x, asteroid[0].rect.y))
            for enemy in collided.items():
                enemy[0].new_shield()

            collided = pygame.sprite.groupcollide(p3enemy_spawner.enemy_group2, p3enemy_spawner.sdeltaasteroid_group, False,
                                                  True)  ## seperate badguy1 as alt1 grou# p
            for enemy, asteroid in collided.items():
                ##shield_spawner.spawn_shipshield((player.rect.x, player.rect.y))
                asteroid[0].get_hit()
                if asteroid[0].is_destroyed:
                    explosion_spawner.spawn_p1asteroidexplosions((asteroid[0].rect.x, asteroid[0].rect.y))
            for enemy in collided.items():
                enemy[0].new_shield()



        



def intro():
    display = pygame.display.set_mode(c.display_size)
    black = (0, 0, 0)
    display.fill(black)
    run = True
    ready_text = pygame.image.load("Welcome_Text.png")
    bg1 = BG1()
    bg1_group = pygame.sprite.Group()
    bg1_group.add(bg1)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
        display.fill(black)
        ##bg1_group.draw(display)  ## draws background with stars
        display.blit(ready_text, (c.display_width // 7, c.display_height // 3))
        pygame.display.update()
        ##bg1_group.update()


def game_over():
    display = pygame.display.set_mode(c.display_size)
    black = (0, 0, 0)
    display.fill(black)
    run = True
    game_over_text = pygame.image.load("gave_over_text.png")
    bg1 = BG1()
    bg1_group = pygame.sprite.Group()
    bg1_group.add(bg1)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
        display.fill(black)
       ##bg1_group.draw(display)  ## draws background with stars
        display.blit(game_over_text, (c.display_width // 2 - 175, c.display_height // 2 - 65))
        pygame.display.update()
        ##bg1_group.update()




intro()



