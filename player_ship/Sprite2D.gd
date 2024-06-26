extends Sprite2D

@export var gold_texture = preload("res://assets/barrel_roll_gold_1.png")
@export var regular_texture = preload("res://assets/barrel_roll.png")
##@export var txtr = self.texture

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	texture = regular_texture


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
