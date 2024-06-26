class_name MoveComponent
extends Node

@export var actor: Node2D
@export var velocity: Vector2

##@export var current_animation: String = "default"


func _process(delta: float) -> void:
	actor.translate(velocity * delta)
	
