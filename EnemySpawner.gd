extends Node


@export var game_stats: GameStats

@onready var alt_enemy = preload("res://Enemies/alt_enemy.tscn")
@onready var target_enemy = preload("res://Enemies/target_enemy.tscn")
var margin = 8
var screen_width = ProjectSettings.get_setting("display/window/size/viewport_width")
@export var alt_count = 0
@export var target_count = 0




func spawn_enemies(enemy_type): 
	if enemy_type == alt_enemy:
		var altinst = alt_enemy.instantiate()
		add_child(altinst)
		altinst.position = Vector2(randf_range(margin, screen_width), -5)
		game_stats.alt_count += 1
	elif enemy_type == target_enemy:
		var targetinst = target_enemy.instantiate()
		add_child(targetinst)
		targetinst.position = Vector2(randf_range(margin, screen_width), -5)
		game_stats.target_count += 1
