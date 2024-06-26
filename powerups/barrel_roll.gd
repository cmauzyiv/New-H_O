class_name BarrelRoll
extends Node2D



@onready var stats_component:  = $StatsComponent as StatsComponent
@onready var visible_on_screen_notifier_2d: VisibleOnScreenNotifier2D = $VisibleOnScreenNotifier2D
@onready var hurtbox_component:  = $HurtboxComponent as HurtboxComponent
@onready var animation_hit_box_component:  = $AnimationHitBoxComponent as AnimationHitBoxComponent
@onready var score_component:  = $ScoreComponent as ScoreComponent



var margin = 8
var screen_width = ProjectSettings.get_setting("display/window/size/viewport_width")

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	visible_on_screen_notifier_2d.screen_exited.connect(queue_free)
	stats_component.no_health.connect(func():
		score_component.adjust_powerups()
		queue_free()
	)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
