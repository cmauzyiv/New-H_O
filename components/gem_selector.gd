class_name GemSelectorComponent
extends Node

@export var gem_color: int = 0:
		set(value):
			gem_color = value
		
			color_changed.emit()
		
		
signal color_changed()

