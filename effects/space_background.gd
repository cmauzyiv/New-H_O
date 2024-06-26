extends ParallaxBackground

@onready var space_layer: ParallaxLayer = %SpaceLayer
@onready var far_stars_layer: ParallaxLayer = %FarStarsLayer
@onready var close_stars_layer: ParallaxLayer = %CloseStarsLayer
@export var game_stats: GameStats
@onready var p_1_background: TextureRect = $SpaceLayer/P1Background
@onready var p_2_background: TextureRect = $SpaceLayer/P2Background
@onready var p_3_background: TextureRect = $SpaceLayer/P3Background
@onready var p_4_background: TextureRect = $SpaceLayer/P4Background






	
	
func update_background(new_phase: int) -> void:
	if new_phase == 2:
		p_1_background.hide()
		p_2_background.show()
		p_3_background.hide()
		p_4_background.hide()
	if new_phase == 3:
		p_1_background.hide()
		p_2_background.hide()
		p_3_background.show()
		p_4_background.hide()
	if new_phase == 4:
		p_1_background.hide()
		p_2_background.hide()
		p_3_background.hide()
		p_4_background.show()
	
	

func _process(delta: float) -> void:
	space_layer.motion_offset.y += 2 * delta
	far_stars_layer.motion_offset.y += 10 * delta
	close_stars_layer.motion_offset.y += 40 * delta
	
