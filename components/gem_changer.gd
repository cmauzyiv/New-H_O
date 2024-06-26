class_name GemChangerComponent
extends Node

@onready var hurtbox_component: = $"../HurtboxComponent" as HurtboxComponent


# Export the game stats so we can manipulate the game score
@export var game_stats: GameStats



# Export the amount the score should be adjusted
@export var set_gem_color = 0
	


# This is the function that we call to activate this component. By default it will
# Use the adjust_amount when called but we could optionally pass in a different amount.
func adjust_color(amount: int = set_gem_color):
	game_stats.gem_color = amount
	Global.gem_color = amount





