extends Node

onready var http_request = HTTPRequest.new()

func _ready():
	add_child(http_request)
	http_request.connect("request_completed", self, "_on_request_completed")

	var data = "Player behavior data to save"
	var sharepoint_url = "https://your_sharepoint_site/_api/web/GetFolderByServerRelativeUrl('/Shared Documents')/Files/add(overwrite=true, url='data.txt')"
	var access_token = "YOUR_ACCESS_TOKEN"

	upload_to_sharepoint(sharepoint_url, data, access_token)

func upload_to_sharepoint(url: String, data: String, token: String):
	var headers = [
		"Authorization: Bearer " + token,
		"Content-Type: text/plain"
	]

	http_request.request_raw(url, headers, data.to_utf8(), HTTPClient.METHOD_POST)

func _on_request_completed(result, response_code, headers, body):
	if response_code == 200 or response_code == 201:
		print("File uploaded successfully")
	else:
		print("Failed to upload file: ", response_code)
		print("Response body: ", body)
