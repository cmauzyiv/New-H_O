class_name SaveDataComponent
extends Node

@export var game_stats: GameStats

var save_path = "user://data.save"




var data = "Total Shots: " + str(game_stats.total_shots) + "\n"

func save_data() -> void:
	var file = FileAccess.open(save_path, FileAccess.WRITE)
	file.store_string(data)


