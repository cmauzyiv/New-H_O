extends Node2D


@onready var right_muzzle: Marker2D = $RightMuzzle
@onready var spawner_component: SpawnerComponent = $SpawnerComponent as SpawnerComponent
@onready var fire_rate_timer: Timer = $FireRateTimer
@onready var move_component: MoveComponent = $MoveComponent as MoveComponent
@onready var animation_component:  = $AnimationComponent as AnimationComponent
@onready var hitbox_component: HitboxComponent = $HitboxComponent as HitboxComponent
@onready var shield_animated: AnimatedSprite2D = $Anchor/ShieldAnimated
@onready var stats_component:  = $StatsComponent as StatsComponent
@onready var hurtbox_component:  = $HurtboxComponent as HurtboxComponent
@onready var score_component:  = $ScoreComponent as ScoreComponent



##func _ready() -> void:
	##hurtbox_component.hurt.connect(bounce())



var fire_ready := false


func prepare_lasers() -> void:
	if Input.is_action_just_pressed("ui_shoot"):
		if !fire_ready:
			fire_ready = true
			fire_lasers()
			await get_tree().create_timer(.25).timeout
			fire_ready = false

func fire_lasers() -> void:
	spawner_component.spawn(right_muzzle.global_position)
	score_component.adjust_total_shots()
	Global.stream.append(9) 
	


func bounce() -> void:
	pass
	
func _ready() -> void:
	hurtbox_component.hurt.connect(shield_animated.play_shield.unbind(1))

func _process(delta: float) -> void:
	prepare_lasers()
		
		

		

