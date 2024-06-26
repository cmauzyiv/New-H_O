# Give the component a class name so it can be instanced as a custom node
class_name AnimationHitBoxComponent
extends Area2D

# Export the damage amount this hitbox deals
@export var animation = 0
@export var texture = 0


# Create a signal for when the hitbox hits a hurtbox
signal animate_hurtbox(hurtbox)
signal texture_hurtbox(hurtbox)

func _ready():
	# Connect on area entered to our hurtbox entered function
	area_entered.connect(_on_hurtbox_entered)

func _on_hurtbox_entered(hurtbox: HurtboxComponent):
	# Make sure the area we are overlapping is a hurtbox
	if not hurtbox is HurtboxComponent: return
	# Make sure the hurtbox isn't invincible
	if hurtbox.is_invincible: return
	# Signal out that we hit a hurtbox (this is useful for destroying projectiles when they hit something)
	if animation > 0:
		animate_hurtbox.emit(hurtbox)
		hurtbox.animate.emit(self)
	if texture >= 1:
		texture_hurtbox.emit(hurtbox)
		hurtbox.texture.emit(self)
	# Have the hurtbox signal out that it was hit
	

	
	

