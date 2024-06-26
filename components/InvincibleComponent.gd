class_name InvincibleComponent
extends Node
@onready var hurtbox_component:  = $"../HurtboxComponent" as HurtboxComponent

@onready var game_stats = preload("res://game_stats.tres")
 
@export var invincible_phase = 0
		


func check_invincible():
	if game_stats.phase == invincible_phase:
		hurtbox_component.is_invincible
		


