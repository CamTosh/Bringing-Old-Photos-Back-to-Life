import os
from flask import jsonify, request
from flask import current_app
from . import routes
from worker import start
import uuid

@routes.route("/status/<string:id>", methods=['GET'])
def status(id: str):
	outputDir = os.path.join(current_app.config["IMAGE_OUTPUTS"], id)
	if not os.path.exists(outputDir):
		return 'path not exist yet'

	folders = os.listdir(outputDir)
	if 'final_output' in folders:
		result = os.listdir(os.path.join(outputDir, 'final_output'))
		return jsonify({'final_output': result})

	return jsonify({'folders': folders})


@routes.route("/transform", methods=['POST'])
def transformRoute():
	if not request.data:
		return 'curl -X POST --upload-file maison.png http://127.0.0.1:5000/transform'

	id = str(uuid.uuid4())

	inputPath = os.path.join(current_app.config["IMAGE_UPLOADS"], id)
	os.mkdir(inputPath)

	outputPath = os.path.join(current_app.config["IMAGE_OUTPUTS"], id)
	os.mkdir(outputPath)

	with open(os.path.join(inputPath, '1.png'), 'wb') as f:
		f.write(request.data)

	start(id)

	return id