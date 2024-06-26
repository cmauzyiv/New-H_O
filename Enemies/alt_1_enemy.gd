class_name Alt1Enemy
extends Enemy


@onready var states: Node = $States

@onready var move_down_state:  = %MoveDownState as TimedStateComponent
@onready var move_side_state:  = %MoveSideState as TimedStateComponent
@onready var pause_state: = %PauseState as TimedStateComponent
@onready var move_side_component:  = %MoveSideComponent as MoveComponent
@onready var projectile_spawner_component:  = %ProjectileSpawnerComponent as SpawnerComponent
@onready var fire_state: = %FireState as StateComponent



func _ready() -> void:
	super()
	
	for state in states.get_children(): ## loop through all states
		state = state as StateComponent #this only made it so we could autocomplete
		state.disable()
		
	
		
	

		
	move_down_state.state_finished.connect(enable_move_side) #when move down state is finished, start the move side state
	move_side_state.state_finished.connect(enable_fire_state)
	fire_state.state_finished.connect(enable_pause_state)
	pause_state.state_finished.connect(enable_move_down_state)

	
	##move_down_state.enable()
	
	enable_move_down_state()
		
func enable_move_side() -> void:
		move_side_state.enable()
		move_side_component.velocity.x = [-20, 20].pick_random()

func enable_fire_state() -> void:
		move_side_component.velocity.x = 0
		fire_state.enable()
		projectile_spawner_component.spawn(global_position)
		fire_state.disable()
		fire_state.state_finished.emit()

func enable_pause_state() -> void:
	move_side_component.velocity.x = 0
	pause_state.enable()
	
func enable_move_down_state() -> void:
	move_down_state.enable()
	move_side_component.velocity.x = 0

func _process(delta: float) -> void:
	print(move_side_component.velocity.x)

	animate_the_ship()
	
	
func animate_the_ship() -> void:
	if move_side_component.velocity.x < 0:
		animated_sprite_2d.play("bank_left")
	elif move_side_component.velocity.x > 0:
		animated_sprite_2d.play("bank_right")
	else:
		animated_sprite_2d.play("center")
