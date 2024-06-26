class_name HyperSpeedComponent
extends Node

# Export the actor this component will operate on
@export var actor: Node2D

# Grab access to the stats so we can tell when the health has reached zero
@export var hurtbox_component: HurtboxComponent

# Export and grab access to a spawner component so we can create an effect on death
@export var effect_spawner_component: SpawnerComponent

func _ready() -> void:
	# Connect the the no health signal on our stats to the destroy function
	hurtbox_component.animate.connect(func(animation_hit_box_component: AnimationHitBoxComponent):
		if animation_hit_box_component.animation == 3:
			
			await get_tree().create_timer(5).timeout
			
	)
func destroy() -> void:
	# create an effect (from the spawner component) and free the actor
	destroy_effect_spawner_component.spawn(actor.global_position)
	actor.queue_free()
