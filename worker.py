from flask import current_app
import os

# Start transform process
def start(id):
    transformCmd = (
        "/usr/local/bin/python3.8 run.py --input_folder"
        + os.path.join(current_app.config["IMAGE_UPLOADS"], id)
        + " --outputs_dir "
        + os.path.join(current_app.config["IMAGE_OUTPUTS"], id)
        + " --gpu_ids 1" # TODO check unsued gpu with cuda api
 	)
    os.system(transformCmd)
