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

collided = pygame.sprite.groupcollide(sprite_group, p2enemy_spawner.spin_group, False, True)
for player, powerup in collided.items():
    player.turning_left = False
    player.turning_right = False
    player.spinning = True

collided = pygame.sprite.groupcollide(sprite_group, p2enemy_spawner.speed_group, False, True)
for player, powerup in collided.items():
    player.fast = True

collided = pygame.sprite.groupcollide(sprite_group, p2enemy_spawner.max_gems_group, False, True)
for player, powerup in collided.items():
    p2enemy_spawner.max_generate = True
    p2enemy_spawner.p2asteroid_timer = 0

collided = pygame.sprite.groupcollide(sprite_group, p2enemy_spawner.roll_group, False, True)
for player, powerup in collided.items():
    if player.turning_left:
        player.rolling_left = True
    elif player.turning_right:
        player.rolling_right = True
    else:
        player.rolling_right = True
    player.turning_left = False
    player.turning_right = False
    player.spinning = False

collided = pygame.sprite.groupcollide(sprite_group, p2enemy_spawner.p2asteroid_group, False,
                                      True)  ## seperate badguy1 as alt1 group
for player, asteroid in collided.items():
    ##shield_spawner.spawn_shipshield((player.rect.x, player.rect.y))

    asteroid[0].get_hit()

    if asteroid[0].is_destroyed:
        asteroids += 1
        stream.append(5)
        explosion_spawner.spawn_p1asteroidexplosions((asteroid[0].rect.x, asteroid[0].rect.y))
        player.hud.asteroid_score.update_score(asteroid[0].point_value)

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

            collided = pygame.sprite.groupcollide(sprite_group, p3enemy_spawner.spin_group, False, True)
            for player, powerup in collided.items():
                player.turning_left = False
                player.turning_right = False
                player.spinning = True

            collided = pygame.sprite.groupcollide(sprite_group, p3enemy_spawner.speed_group, False, True)
            for player, powerup in collided.items():
                player.fast = True

            collided = pygame.sprite.groupcollide(sprite_group, p3enemy_spawner.max_gems_group, False, True)
            for player, powerup in collided.items():
                p3enemy_spawner.max_generate = True
                p3enemy_spawner.asteroid_timer = 0

            collided = pygame.sprite.groupcollide(sprite_group, p3enemy_spawner.roll_group, False, True)
            for player, powerup in collided.items():
                if player.turning_left:
                    player.rolling_left = True
                elif player.turning_right:
                    player.rolling_right = True
                else:
                    player.rolling_right = True
                player.turning_left = False
                player.turning_right = False
                player.spinning = False

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