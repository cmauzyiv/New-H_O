class_name MaxGems
extends Node2D


@onready var stats_component:  = $StatsComponent as StatsComponent
@onready var visible_on_screen_notifier_2d: VisibleOnScreenNotifier2D = $VisibleOnScreenNotifier2D
@onready var hurtbox_component:  = $HurtboxComponent as HurtboxComponent
@onready var max_gems_timer: Timer = $MaxGemsTimer
@onready var powerup_image: Sprite2D = $Sprite2D
@onready var score_component: = $ScoreComponent as ScoreComponent





var margin = 8
var screen_width = ProjectSettings.get_setting("display/window/size/viewport_width")

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	visible_on_screen_notifier_2d.screen_exited.connect(queue_free)
	stats_component.no_health.connect(func():
		score_component.adjust_powerups()
		enable_global_max_gems()
		await get_tree().create_timer(6).timeout
		Global.max_gems = false
		queue_free()
		
		)
	
	
	


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func enable_global_max_gems() -> void:
	Global.max_gems = true
	##max_gems_timer.start()
	powerup_image.visible = false
	SignalManager.max_gems_turned_on.emit()
	##max_gems_timer.timeout.connect(disable_global_max_gems)
func disable_global_max_gems() -> void:
	Global.max_gems = false
	queue_free()
	



