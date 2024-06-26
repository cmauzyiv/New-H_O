class_name AnimationComponent
extends Node

@onready var move_component: = $"../MoveComponent" as MoveComponent



##@export var default_animation = 0
##@export var left_animation = 1
##@export var right_animation  = 2
##@export var barrel_roll = 3
##@export var spin = 4
@export var hurtbox_component: HurtboxComponent


##@export var animations : AnimatedSprite2D
@onready var animation_player: AnimationPlayer = $"../AnimationPlayer"




@export var gold_texture = preload("res://assets/barrel_roll_gold_1.png")
@export var regular_texture = preload("res://assets/barrel_roll.png")
@export var blue_texture = preload("res://assets/barrel_roll_blue_1.png")
@export var red_texture = preload("res://assets/barrel_roll_red_1.png")
@export var green_texture = preload("res://assets/barrel_roll_green_1.png")

@onready var main_ship: Sprite2D = $"../Anchor/Sprite2D"


##var txtr = sprite_2d.texture
@export var current_animation = 0
@export var current_texture = 1
var animating = false
var idle = true
var turn_left = false
var turn_right = false
var hold_left = false
var hold_right = false
var barrel_roll_left = false
var barrel_roll_right = false


##@export var current_animation: String = "default"

func animate_the_ship() -> void:
	if current_animation == 1:
		if turn_right == true:
			if animation_player.current_animation == "hold_right":
				animation_player.play("barrel_right")
		elif turn_left == true:
			if animation_player.current_animation == "hold_left":
				animation_player.play("barrel_left")
		else:
			animation_player.play("barrel_right")
	elif current_animation == 2:
		if turn_right == true:
			if animation_player.current_animation == "hold_right":
				animation_player.play("spin")
		elif turn_left == true:
			if animation_player.current_animation == "hold_left":
				animation_player.play("spin")
		else:
			animation_player.play("spin")
	else:
		if move_component.velocity.x < 0:
			turn_right = false
			turn_left = true
			if animation_player.current_animation != "hold_left":
				animation_player.play("bank_left")
		elif move_component.velocity.x > 0:
			turn_left = false
			turn_right = true
			if animation_player.current_animation != "hold_right":
				animation_player.play("bank_right")
		else:
			turn_right = false
			turn_left = false
			animation_player.play("idle")
		
	
func texture_the_ship() -> void:
	if current_texture == 1:
		main_ship.texture = regular_texture
	if current_texture == 2:
		main_ship.texture = gold_texture
	if current_texture == 3:
		main_ship.texture = blue_texture
	if current_texture == 4:
		main_ship.texture = red_texture
	if current_texture == 5:
		main_ship.texture = green_texture



func _ready() -> void:
	hurtbox_component.animate.connect(func(animation_hit_box_component: AnimationHitBoxComponent):
		current_animation = animation_hit_box_component.animation
		)
	hurtbox_component.texture.connect(func(animation_hit_box_component: AnimationHitBoxComponent):
		if animation_hit_box_component.texture >= 1:
			current_texture = randi_range(1,5)
			
		)
		
	
			
	

	
func _process(delta: float) -> void:
	animate_the_ship()
	texture_the_ship()
	print(current_animation)
	
	






func _on_animation_player_animation_finished(anim_name: StringName) -> void:
	if anim_name == "bank_left":
		animation_player.play("hold_left")
	elif anim_name == "bank_right":
		animation_player.play("hold_right")
	elif anim_name == "barrel_left":
		current_animation = 0
	elif anim_name == "barrel_right":
		current_animation = 0
	elif anim_name == "spin":
		current_animation = 0

