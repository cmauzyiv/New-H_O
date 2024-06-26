extends Node2D

@export var game_stats: GameStats

@onready var ship: Node2D = $Ship
@onready var alt_enemy = preload("res://Enemies/alt_enemy.tscn")
@onready var target_enemy = preload("res://Enemies/target_enemy.tscn")
var margin = 8
var screen_width = ProjectSettings.get_setting("display/window/size/viewport_width")
##@export var alt_count = 0
##@export var target_count = 0
@onready var enemy_spawner: Node2D = $enemy_spawner 
@onready var score_label: Label = $ScoreLabel
@onready var space_background: ParallaxBackground = $SpaceBackground
@onready var pink_label: Label = $Control/HBoxContainer3/PinkLabel
@onready var green_label: Label = $Control/HBoxContainer/GreenLabel
@onready var blue_label: Label = $Control/HBoxContainer2/BlueLabel
@onready var power_up_generator: Node2D = $PowerUpGenerator
@onready var shake_component:  = $ShakeComponent as ShakeComponent
@onready var session_number = 1

@onready var stream_timer: Timer = $StreamTimer
@onready var seconds = 0



var data_save_path = "res://data.txt"
var stream_save_path = "res://stream.txt"



@onready var data: String

func _ready() -> void:
	randomize()
	game_stats.phase = 1
	##text1 = $total_shots/text1
	
	SignalManager.max_gems_turned_on.connect(on_max_turned_on)
	game_stats.score_changed.connect(update_score_label)
	update_score_label(game_stats.score)
	game_stats.green_gems_changed.connect(update_green_gem_label)
	update_green_gem_label(game_stats.green_gems)
	game_stats.pink_gems_changed.connect(update_pink_gem_label)
	update_pink_gem_label(game_stats.pink_gems)
	game_stats.blue_gems_changed.connect(update_blue_gem_label)
	update_blue_gem_label(game_stats.blue_gems)

	game_stats.alt_count_changed.connect(enemy_spawner.check_alt_counts)
	game_stats.target_count_changed.connect(enemy_spawner.check_target_counts)
	##game_stats.score_changed.connect(func(new_score: int):
		##if new_score >= 15:
			##game_stats.phase = 2
		##)

	game_stats.phase_changed.connect(space_background.update_background)
	
	ship.tree_exiting.connect(func():
		await get_tree().create_timer(1.0).timeout
		get_tree().change_scene_to_file(("res://Menus/game_over.tscn"))
	)


	
func _process(delta: float) -> void:
	pass
	
	##print(game_stats.alt_count)
		

func update_score_label(new_score: int) -> void:
	score_label.text = "Score: " + str(new_score)
func update_pink_gem_label(new_pink_gems: int) -> void:
	pink_label.text = "Pink: " + str(new_pink_gems)
func update_green_gem_label(new_green_gems: int) -> void:
	green_label.text = "Green: " + str(new_green_gems)
func update_blue_gem_label(new_blue_gems: int) -> void:
	blue_label.text = "Blue: " + str(new_blue_gems)
	
var data_file = FileAccess.open(data_save_path, FileAccess.WRITE)
var stream_file = FileAccess.open(stream_save_path, FileAccess.WRITE)

func update_stream() -> void:
	stream_file.store_line(str(seconds) + str(Global.stream) + "\n")

	Global.stream = []

func save_data() -> void:
	data_file.store_line("\n")
	data_file.store_line("Phase = ")
	if game_stats.phase == 1:
		data_file.store_string("Baseline" + "\n")

	elif game_stats.phase == 2:
		data_file.store_string("Treatment" + "\n")
	elif game_stats.phase == 1:
		data_file.store_string("SD" + "\n")
	elif game_stats.phase == 4:
		data_file.store_string("Extinction" + "\n")
	data_file.store_line("Session Num = " + str(session_number) + "\n")
	data_file.store_line("target responses = " + str(game_stats.target_responses) + "\n")
	if game_stats.phase >= 2:
		data_file.store_line("alternative responses = " + str(game_stats.alt_responses)+ "\n")
	data_file.store_string("total shots = " + str(game_stats.total_shots) + "\n")
	data_file.store_string("gems collected = " + str(game_stats.total_gems) + "\n")
	data_file.store_string("total score = " + str(game_stats.score) + "\n")
	data_file.store_string("Power Ups: " + "\n")
	data_file.store_string("barrel rolls = " + str(game_stats.barrel_rolls) + "\n")
	data_file.store_string("spins = " + str(game_stats.spins) + "\n")
	data_file.store_string("gem boost = " + str(game_stats.max_gems) + "\n")
	data_file.store_string("speed boost = " + str(game_stats.speed_boost) + "\n")
	data_file.store_string("gem changers = " + str(game_stats.gem_changer) + "\n")
	data_file.store_string("textures = " + str(game_stats.textures) + "\n")
	
	
	
	game_stats.total_shots = 0
	game_stats.target_responses = 0
	game_stats.alt_responses = 0
	game_stats.total_shots = 0
	game_stats.total_gems = 0
	game_stats.barrel_rolls = 0
	game_stats.spins = 0
	game_stats.speed_boost = 0
	game_stats.gem_changer = 0
	game_stats.textures = 0
	game_stats.max_gems = 0
	
	
	
	
	print("data saved")

##func load_game():
##	var data_file = FileAccess.open(save_path,FileAccess.READ)
##	data_file.seek_end()
	


func _on_data_timer_timeout() -> void:
	save_data()
	set_session()

func on_max_turned_on():
	shake_component.tween_shake()
	
func set_session() -> void:
	if session_number == 3:
		game_stats.phase = 2
	elif session_number == 6:
		game_stats.phase = 4
	elif session_number == 9:
		get_tree().change_scene_to_file(("res://Menus/game_over.tscn"))
	session_number += 1
	
	
		
	



func _on_stream_timer_timeout() -> void:
	seconds += 1 # Replace with function body.
	update_stream()
	if seconds == 60:
		seconds = 0
