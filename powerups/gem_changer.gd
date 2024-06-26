class_name GemChanger
extends Node2D


@onready var stats_component:  = $StatsComponent as StatsComponent
@onready var visible_on_screen_notifier_2d: VisibleOnScreenNotifier2D = $VisibleOnScreenNotifier2D
@onready var hurtbox_component:  = $HurtboxComponent as HurtboxComponent
@onready var hitbox_component:  = $HitboxComponent as HitboxComponent
@onready var score_component:  = $ScoreComponent as ScoreComponent

@onready var destroyed_component: = $DestroyedComponent as DestroyedComponent
@onready var gem_changer_component: = $GemChangerComponent as GemChangerComponent


@export var game_stats: GameStats
@onready var animated_sprite_2d: AnimatedSprite2D = $AnimatedSprite2D

var margin = 8
var screen_width = ProjectSettings.get_setting("display/window/size/viewport_width")

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	stats_component.no_health.connect(func():
		gem_changer_component.adjust_color()
		score_component.adjust_powerups()
		queue_free()
		)
	visible_on_screen_notifier_2d.screen_exited.connect(queue_free)
	
	
	##hitbox_component.hit_hurtbox.connect(gem_changer_component.adjust_color.unbind(1))
	##hitbox_component.hit_hurtbox.connect(destroyed_component.destroy.unbind(1))



# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
