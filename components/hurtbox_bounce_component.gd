class_name HurtboxBounceComponent
extends Node


@export var actor: Node2D

# We need to grab the move component of the actor in order to change its velocity when bouncing
@export var move_component: MoveComponent
@export var hurtbox_component: HurtboxComponent



func _ready() -> void:
	# Connect the hurt signal on the hurtbox component to an anonymous function
	# that removes health equal to the damage from the hitbox
	hurtbox_component.hurt.connect(func(hitbox_component: HitboxComponent):
		if actor.global_position < hitbox_component.global_position:
			move_component.velocity = move_component.velocity.bounce(Vector2.UP)
			move_component.velocity = move_component.velocity.bounce(Vector2.LEFT)
		if actor.global_position > hitbox_component.global_position:
			move_component.velocity = move_component.velocity.bounce(Vector2.DOWN)
			move_component.velocity = move_component.velocity.bounce(Vector2.RIGHT)
			
			)
		##if actor.global_position.x > hitbox_component.global_position.x:
		##	move_component.velocity = move_component.velocity.bounce(Vector2.LEFT)
		##if actor.global_position.y < hitbox_component.global_position.y:
		##	move_component.velocity = move_component.velocity.reflect(Vector2.UP)
		##if actor.global_position.y > hitbox_component.global_position.y:
		##	move_component.velocity = move_component.velocity.reflect(Vector2.DOWN))
