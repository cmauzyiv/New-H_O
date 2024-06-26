extends Node




var gem_color = 0
@export var max_gems = false

var screen_width = ProjectSettings.get_setting("display/window/size/viewport_width")
var screen_height = ProjectSettings.get_setting("display/window/size/viewport_height")
var half_screen = screen_width / 2
var left_boundary = 75
var right_boundary = screen_width - 75
var top_boundary = 75
var bottom_boundary = screen_height - 75
var stream = []

