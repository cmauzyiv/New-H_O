# Give the component a class name so it can be instanced as a custom node
class_name CounterComponent


extends Node

# Export the game stats so we can manipulate the game score
@export var world_stats: WorldStats

# Export the amount the score should be adjusted
@export var adjust_amount = 1

# This is the function that we call to activate this component. By default it will
# Use the adjust_amount when called but we could optionally pass in a different amount.
func adjust_count(amount: int = adjust_amount):
	world_stats.score -= amount
