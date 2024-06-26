class_name HealthTimerComponent
extends Node

@export var stats_component: StatsComponent
@onready var timer = $Timer









# Grab a hurtbox so we know when we have taken a hiet


func timer_start():
	timer.start(randf_range(5,10))
	

	
	

	
# Called every frame. 'delta' is the elapsed time since the previous frame.
