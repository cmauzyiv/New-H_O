# Give the component a class name so it can be instanced as a custom node
class_name TimedStateComponent

# Extend the state
extends StateComponent

# This component is used to create a state that automatically disables itself after
# a duration

# Export the duration for this state
var duration = randf_range(2,3)

# Create a new timer
var timer: = Timer.new()

func _ready() -> void:
	# Add the timer as a child so we can use it
	randomize()
	add_child(timer)
	
	
	# Connect to the timeout functino on the timer
	timer.timeout.connect(func():
		# Emit finished because this state is finished
		state_finished.emit()
		
		# Disable this state
		disable()
	)
	
	# Start the timer whenever this state is enabled
	enabled.connect(timer.start.bind(duration))
