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
if time_count == 3600:
    if phase == 3:
        pass
    else:
        record_data()
    if trial_num == 4:
        player.hud.asteroid_score.value = 0
        player.hud.asteroid_score.update_score(0)
        phase = 2
    elif trial_num == 8:
        player.hud.asteroid_score.value = 0
        player.hud.asteroid_score.update_score(0)
        phase = 3
        trial_num += 1
    elif trial_num == 18:
        phase = 5
    if phase == 3:
        pass
    else:
        trial_num += 1
    time_count = 0

if phase == 3:
    if trial_type == 0:
        long_sd1_timer -= 1
        if long_sd1_timer == 0:
            record_data()
            player.hud.asteroid_score.value = 0
            player.hud.asteroid_score.update_score(0)
            trial_type = 1
            long_sdelta_timer = 18000
    elif trial_type == 1:
        long_sdelta_timer -= 1
        if long_sdelta_timer == 0:
            record_data()
            player.hud.asteroid_score.value = 0
            player.hud.asteroid_score.update_score(0)
            trial_type = 2
            long_sd2_timer = 9000
    elif trial_type == 2:
        long_sd2_timer -= 1
        if long_sd2_timer == 0:
            record_data()
            if trial_num == 13:
                phase = 4
                player.hud.asteroid_score.value = 0
                player.hud.asteroid_score.update_score(0)
                trial_num += 1
            else:
                trial_type = 0
                trial_num += 1
                long_sd1_timer = 9000