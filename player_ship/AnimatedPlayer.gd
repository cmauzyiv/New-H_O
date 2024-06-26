extends AnimatedSprite2D
@export var current_animation = 0
var animating = false


##@export var current_animation: String = "default"


@onready var move_component:  = $"../../MoveComponent" as MoveComponent

@export var hurtbox_component: HurtboxComponent

func animate_the_ship() -> void:
	if animating == false:
		if move_component.velocity.x < 0:
			play("bank_left")
		elif move_component.velocity.x > 0:
			play("bank_right")
		else:
			play("center")
	


func _ready() -> void:
	hurtbox_component.hurt.connect(func(hitbox_component: HitboxComponent):
		current_animation = hitbox_component.animation
			
	)
		
		
func _process(delta: float) -> void:
	if current_animation > 0:
		animating = true
		if current_animation == 1:
			play_barrel_roll()
		elif current_animation == 2:
			play_spin()
	
func play_barrel_roll() -> void:
	play("barrel_roll")
	animation_finished.connect(func():
		current_animation = 0
		animating = false)
		

	
func play_spin() -> void:
	pass
