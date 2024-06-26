class_name GameStats

extends Resource




var text1



@export var phase: int = 0:
	set(value):
		phase = value
		phase_changed.emit(phase)
		
signal phase_changed(new_phase)

@export var total_shots: int = 0:
	set(value):
		total_shots = value
		
		shots_changed.emit(total_shots)
		

signal shots_changed(new_total_shots)

@export var score: int = 0:
	set(value):
		score = value
		
		score_changed.emit(score) ##everytime score is set, it will emit the score change

@export var highscore: int = 0

signal score_changed(new_score)

@export var alt_count: int = 0:
	set(value):
		alt_count = value
		alt_count_changed.emit(alt_count)
		
signal alt_count_changed(new_alt_count)

@export var alt_responses: int = 0:
	set(value):
		alt_responses = value
		alt_responses_changed.emit(alt_responses)
		
signal alt_responses_changed(new_alt_responses)

@export var target_responses: int = 0:
	set(value):
		target_responses = value
		target_responses_changed.emit(target_responses)
		
signal target_responses_changed(new_target_responses)

@export var target_count: int = 0:
	set(value):
		target_count = value
		target_count_changed.emit(target_count)
		
signal target_count_changed(new_target_count)

@export var green_gems: int = 0:
	set(value):
		green_gems = value
		green_gems_changed.emit(green_gems)

signal green_gems_changed(new_green_gems)

@export var pink_gems: int = 0:
	set(value):
		pink_gems = value
		pink_gems_changed.emit(pink_gems)

signal pink_gems_changed(new_pink_gems)

@export var blue_gems: int = 0:
	set(value):
		blue_gems = value
		blue_gems_changed.emit(blue_gems)

signal blue_gems_changed(new_blue_gems)

@export var total_gems: int = 0:
	set(value):
		total_gems = value
		total_gems_changed.emit(total_gems)
		
		
signal total_gems_changed(new_total_gems)

@export var gem_color: int = 0:
	set(value):
		gem_color = value
		color_changed.emit(gem_color)
		
		
signal color_changed(new_gem_color)

@export var max_gems: int = 0:
	set(value):
		max_gems = value
		max_gems_changed.emit(max_gems)
signal max_gems_changed(new_max_gems)

@export var barrel_rolls: int = 0:
	set(value):
		barrel_rolls = value
		barrel_rolls_changed.emit(barrel_rolls)
		
signal barrel_rolls_changed(new_barrel_rolls)
	

@export var spins: int = 0:
	set(value):
		spins = value
		spins_changed.emit(spins)
signal spins_changed(new_spins)

@export var speed_boost: int = 0:
	set(value):
		speed_boost = value
		speed_boost_changed.emit(speed_boost)
signal speed_boost_changed(new_speed_boost)

@export var textures: int = 0:
	set(value):
		textures = value
		textures_changed.emit(textures)
signal textures_changed(new_textures)

@export var gem_changer: int = 0:
	set(value):
		gem_changer = value
		gem_changer_changed.emit(gem_changer)
signal gem_changer_changed(new_gem_changer)


func _ready():
	pass


	
		
	##else:
		##print("no data saved....")
		##total_shots = 0
