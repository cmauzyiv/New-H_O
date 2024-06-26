class_name TargetEnemy
extends Node2D


@onready var stats_component:  = $StatsComponent as StatsComponent
@onready var visible_on_screen_notifier_2d: VisibleOnScreenNotifier2D = $VisibleOnScreenNotifier2D
@onready var scale_component: ScaleComponent = $ScaleComponent as ScaleComponent
@onready var flash_component: FlashComponent = $FlashComponent as FlashComponent
@onready var shake_component: ShakeComponent = $ShakeComponent as ShakeComponent
@onready var hurtbox_component:  = $HurtboxComponent as HurtboxComponent
@onready var hitbox_component:  = $HitboxComponent as HitboxComponent
@onready var destroyed_component: = $DestroyedComponent as DestroyedComponent
@onready var health_timer_component: = $HealthTimerComponent as HealthTimerComponent
@onready var score_component: = $ScoreComponent as ScoreComponent
@onready var animated_sprite_2d: AnimatedSprite2D = $Anchor/AnimatedSprite2D
@onready var move_down_state:  = %MoveDownState as TimedStateComponent
@onready var move_side_state:  = %MoveSideState as StateComponent
@onready var states: Node = $States
@onready var move_side_component:  = %MoveSideComponent as MoveComponent




var margin = 8
var screen_width = ProjectSettings.get_setting("display/window/size/viewport_width")



func _ready() -> void:
	
	stats_component.no_health.connect(func():
		score_component.adjust_score()
		score_component.decrease_alt_count()
		score_component.decrease_target_count()
		)
	
	visible_on_screen_notifier_2d.screen_exited.connect(queue_free)
	health_timer_component.timer_start()
	##hurtbox_component.hurt.connect(func(hitbox: HitboxComponent):
		##scale_component.tween_scale()
		##flash_component.flash()
		##shake_component.tween_shake()
	##) 
	stats_component.no_health.connect(queue_free)
	
	hitbox_component.hit_hurtbox.connect(destroyed_component.destroy.unbind(1))
	
	for state in states.get_children(): ## loop through all states
		state = state as StateComponent #this only made it so we could autocomplete
		state.disable()
		
	move_down_state.state_finished.connect(enable_move_side) #when move down state is finished, start the move side state



	enable_move_down_state()
		
func enable_move_side() -> void:
	move_side_state.enable()
	move_side_component.velocity.x = [-20, 20].pick_random()

func enable_move_down_state() -> void:
	move_down_state.enable()
	move_side_component.velocity.x = 0
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	animate_the_ship()


func animate_the_ship() -> void:
	if move_side_component.velocity.x < 0:
		animated_sprite_2d.play("bank_left")
	elif move_side_component.velocity.x > 0:
		animated_sprite_2d.play("bank_right")
	else:
		animated_sprite_2d.play("center")


