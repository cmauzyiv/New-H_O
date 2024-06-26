class_name MoveInputComponent
extends Node

@export var move_stats: MoveStats
@export var move_component: MoveComponent ##directly connects with that
@export var hurtbox_component: HurtboxComponent
@onready var animation_component:  = $"../AnimationComponent" as AnimationComponent

@onready var hyperspeed_effect: AnimatedSprite2D = $"../Anchor/AnimatedSprite2D"





func _ready() -> void:
	hurtbox_component.animate.connect(func(animation_hit_box_component: AnimationHitBoxComponent):
		if animation_hit_box_component.animation == 3:
			play_hyperspeed()
			move_stats.speed = 600
			await get_tree().create_timer(5).timeout
			stop_hyperspeed()
			move_stats.speed = 300
			
		)


func _input(event: InputEvent) -> void:
	var input_x_axis = Input.get_axis("ui_left", "ui_right") #get_axis gets value -1, 1 based on what key we are pressin
	var input_y_axis = Input.get_axis("ui_up", "ui_down")
	move_component.velocity = Vector2(input_x_axis * move_stats.speed, input_y_axis * move_stats.speed)

func play_hyperspeed() -> void:
	hyperspeed_effect.visible = true
	hyperspeed_effect.play("default")
	
func stop_hyperspeed() -> void:
	hyperspeed_effect.visible = false
	

	
	
	
##func _on_animation_player_animation_finished() -> void:
##	if name == "default":
##		hyperspeed_effect.play("blank")
## i can have a bunch of ships that all use move_input but they all have their own move_stats
