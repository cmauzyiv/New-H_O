class_name Gems
extends Node2D


@onready var stats_component:  = $StatsComponent as StatsComponent
@onready var visible_on_screen_notifier_2d: VisibleOnScreenNotifier2D = $VisibleOnScreenNotifier2D
@onready var hurtbox_component:  = $HurtboxComponent as HurtboxComponent
@onready var hitbox_component:  = $HitboxComponent as HitboxComponent
@onready var destroyed_component: = $DestroyedComponent as DestroyedComponent
@onready var score_component: = $ScoreComponent as ScoreComponent
@onready var animated_sprite_2d: AnimatedSprite2D = $Anchor/AnimatedSprite2D
@export var game_stats: GameStats

var margin = 8
var screen_width = ProjectSettings.get_setting("display/window/size/viewport_width")

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	stats_component.no_health.connect(func():
		score_component.adjust_gem_score())
	visible_on_screen_notifier_2d.screen_exited.connect(queue_free)
	stats_component.no_health.connect(queue_free)
	##hitbox_component.hit_hurtbox.connect(destroyed_component.destroy.unbind(1))
	##hitbox_component.hit_hurtbox.connect(score_component.adjust_gem_score.unbind(1))



# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
