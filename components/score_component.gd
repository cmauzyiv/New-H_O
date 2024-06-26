# Give the component a class name so it can be instanced as a custom node
class_name ScoreComponent
extends Node

@onready var hurtbox_component:  = $"../HurtboxComponent" as HurtboxComponent

# Export the game stats so we can manipulate the game score
@export var game_stats: GameStats
@export var invincible_phase: int = 0:
	set(value):
		invincible_phase = value 


# Export the amount the score should be adjusted
@export var adjust_amount = 5
@export var adjust_shots = 1
@export var adjust_alt_responses_amount = 0
@export var adjust_target_responses_amount = 0
@export var adjust_alt_amount = 0
@export var adjust_target_amount = 0
@export var adjust_green_gem_amount = 0
@export var adjust_pink_gem_amount = 0
@export var adjust_blue_gem_amount = 0
@export var adjust_max_gems_amount = 0
@export var adjust_total_gems_amount = 0
@export var adjust_barrel_rolls_amount = 0
@export var adjust_spins_amount = 0
@export var adjust_gem_changer_amount = 0
@export var adjust_textures_amount = 0
@export var adjust_speed_boost_amount = 0


# This is the function that we call to activate this component. By default it will
# Use the adjust_amount when called but we could optionally pass in a different amount.
func adjust_score(amount: int = adjust_amount):
	game_stats.score += amount
	
func increase_alt_count(amount: int = adjust_alt_amount):
	game_stats.alt_count += amount

func decrease_alt_count(amount: int = adjust_alt_amount):
	game_stats.alt_count -= amount
	
func increase_target_count(amount: int = adjust_target_amount):
	game_stats.target_count += amount
	
func decrease_target_count(amount: int = adjust_target_amount):
	game_stats.target_count -= amount

func adjust_gem_score(green_amount: int = adjust_green_gem_amount, pink_amount: int = adjust_pink_gem_amount, blue_amount: int = adjust_blue_gem_amount, total_amount: int = adjust_total_gems_amount):
	Global.stream.append("gem")
	game_stats.green_gems += green_amount
	game_stats.pink_gems += pink_amount
	game_stats.blue_gems += blue_amount
	game_stats.total_gems += total_amount

func adjust_total_shots(amount: int = adjust_shots):
	game_stats.total_shots += amount
	
func adjust_responses(target_amount: int = adjust_target_responses_amount, alt_amount: int = adjust_alt_responses_amount ):
	if target_amount >= 1:
		game_stats.target_responses += target_amount
		Global.stream.append("target_resp")
	elif alt_amount >= 1:
		game_stats.alt_responses += alt_amount
		Global.stream.append("alt_resp")
	
func adjust_powerups(barrel_roll_amount: int = adjust_barrel_rolls_amount, spins_amount: int = adjust_spins_amount,
max_gems_amount: int = adjust_max_gems_amount, textures_amount: int = adjust_textures_amount, gem_changer_amount: int = adjust_gem_changer_amount, 
speed_boost_amount: int = adjust_speed_boost_amount):
	if barrel_roll_amount >= 1:
		game_stats.barrel_rolls += barrel_roll_amount
		Global.stream.append("barrel_roll")
	elif max_gems_amount >= 1:
		game_stats.max_gems += max_gems_amount
		Global.stream.append("gem boost")
	elif spins_amount >= 1:
		game_stats.spins += spins_amount
		Global.stream.append("spin")
	elif gem_changer_amount >= 1:
		game_stats.gem_changer += gem_changer_amount
		Global.stream.append("gem_changer")
	elif speed_boost_amount >= 1:	
		game_stats.speed_boost += speed_boost_amount
		Global.stream.append("speed boost")
	elif textures_amount >= 1:
		game_stats.textures += textures_amount
		Global.stream.append("texture change")

	




