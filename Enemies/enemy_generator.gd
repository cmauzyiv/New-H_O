extends Node2D

@export var PinkGemScene: PackedScene
@export var GreenGemScene: PackedScene
@export var BlueGemScene: PackedScene
@export var GreenChangerScene: PackedScene
@export var BlueChangerScene: PackedScene
@export var PinkChangerScene: PackedScene
@export var BarrelRollScene: PackedScene
@export var SpinScene: PackedScene
@export var GoldTextureScene: PackedScene
@export var RainbowTextureScene: PackedScene
@export var MaxGemsScene: PackedScene
@export var HyperspeedScene: PackedScene

##@export var stats_component: StatsComponent


@export var game_stats: GameStats


var margin = 8
var screen_width = ProjectSettings.get_setting("display/window/size/viewport_width")




@onready var spawner_component:  = $SpawnerComponent as SpawnerComponent
@onready var pink_gem_spawn_timer: Timer = $PinkGemSpawnTimer
@onready var green_gem_spawn_timer: Timer = $GreenGemSpawnTimer
@onready var blue_gem_spawn_timer: Timer = $BlueGemSpawnTimer
@onready var gem_changer_spawn_timer: Timer = $GemChangerSpawnTimer
@onready var green_changer_spawn_timer: Timer = $GreenChangerSpawnTimer
@onready var gem_changer_timer: Timer = $GemChangerTimer
@onready var power_up_timer: Timer = $PowerUpTimer
@onready var gem_spawn_timer: Timer = $GemSpawnTimer
@onready var gem_changer_color = 0
@onready var texture_timer: Timer = $TextureTimer
@onready var max_gems_timer: Timer = $MaxGemsTimer










func select_gems() -> void:
	var rng = RandomNumberGenerator.new()
	var my_random_number = rng.randf_range(0, 100)
	if game_stats.gem_color == 1:
		if my_random_number <= 50:
			gem_changer_color = 2
			handle_spawn(PinkChangerScene)
		elif my_random_number > 50: 
			gem_changer_color = 3
			handle_spawn(BlueChangerScene)
	elif game_stats.gem_color == 2:
		if my_random_number <= 50:
			gem_changer_color = 1
			handle_spawn(GreenChangerScene)
		elif my_random_number > 50: 
			gem_changer_color = 3
			handle_spawn(BlueChangerScene)
	elif game_stats.gem_color == 3:
		if my_random_number <= 50:
			gem_changer_color = 1
			handle_spawn(GreenChangerScene)
		elif my_random_number > 50: 
				gem_changer_color = 2
				handle_spawn(PinkChangerScene)
	else:
		if my_random_number <= 33:
			gem_changer_color = 2
			handle_spawn(PinkChangerScene)
		if (my_random_number > 33 && my_random_number < 66):
			gem_changer_color = 1
			handle_spawn(GreenChangerScene)
		elif my_random_number >= 66:
			gem_changer_color = 3
			handle_spawn(BlueChangerScene)
	gem_changer_timer.start(randf_range(20, 30))
func check_gem_color():
	if Global.max_gems == false:
		if game_stats.gem_color == 1:
			handle_spawn(GreenGemScene)
			gem_spawn_timer.start(randi_range(2, 4))
		elif game_stats.gem_color == 2:
			handle_spawn(PinkGemScene)
			gem_spawn_timer.start(randi_range(2, 4))
		elif game_stats.gem_color == 3:
			handle_spawn(BlueGemScene)
			gem_spawn_timer.start(randi_range(2, 4))
		elif game_stats.gem_color == 0:
			pass
	elif Global.max_gems == true:
		if game_stats.gem_color == 1:
			handle_spawn(GreenGemScene)
			gem_spawn_timer.start(.1)
		elif game_stats.gem_color == 2:
			handle_spawn(PinkGemScene)
			gem_spawn_timer.start(.1)
		elif game_stats.gem_color == 3:
			handle_spawn(BlueGemScene)
			gem_spawn_timer.start(.1)
		elif game_stats.gem_color == 0:
			pass
		
func select_powerup():
	var rng_1 = RandomNumberGenerator.new()
	var my_random_number_1 = rng_1.randi_range(1, 5)
	if my_random_number_1 == 1:
		handle_spawn(BarrelRollScene)
		power_up_timer.start(randf_range(5, 10))
	elif my_random_number_1 == 2:
		handle_spawn(SpinScene)
		power_up_timer.start(randf_range(5, 10))
	elif my_random_number_1 == 3:
		handle_spawn(MaxGemsScene)
		power_up_timer.start(randf_range(5, 10))
	elif my_random_number_1 == 4:
		handle_spawn(RainbowTextureScene)
		power_up_timer.start(randf_range(5, 10))
	elif my_random_number_1 == 5:
		handle_spawn(HyperspeedScene)
		power_up_timer.start(randf_range(5, 10))
		
	




# Called when the node enters the scene tree for the first time.
func _ready() -> void:	
	gem_changer_timer.timeout.connect(select_gems)
	gem_spawn_timer.timeout.connect(check_gem_color)
	power_up_timer.timeout.connect(select_powerup)




	
	
	
	

func handle_spawn(enemy_scene: PackedScene) -> void:
	spawner_component.scene = enemy_scene
	spawner_component.spawn(Vector2(randf_range(margin, screen_width), 0))
	
	##var spawn_rate = time_offset / (0.5 + (game_stats.score * 0.01))
	
	





