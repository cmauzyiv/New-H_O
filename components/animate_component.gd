# Give the component a class name so it can be instanced as a custom node
class_name AnimateComponent
extends Node

# Grab the stats so we can alter the health
@export var stats_component: StatsComponent

# Grab a hurtbox so we know when we have taken a hiet
@export var hurtbox_component: HurtboxComponent
@onready var move_component:  = $"../MoveComponent" as MoveComponent



func _ready() -> void:
	# Connect the hurt signal on the hurtbox component to an anonymous function
	# that removes health equal to the damage from the hitbox
	hurtbox_component.animate.connect(func(hitbox_component: HitboxComponent):
		stats_component.health -= hitbox_component.damage
		##move_component.current_animation = hitbox_component.animation
		)
