from flask import Flask, render_template, request, jsonify
from PIL import Image
import os
import io
import sys
import numpy as np
import cv2
import base64
from yolo_detection_images import runModel

app = Flask(__name__)

############################################## THE REAL DEAL ###############################################


@app.route('/detectObject', methods=['POST'])
def mask_image():

    # print(request.files , file=sys.stderr)
    file = request.files['image'].read()  # byte file
    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    ######### Do preprocessing here ################
    # img[img > 150] = 0
    # any random stuff do here
    ################################################

    img, person_count, chair_count, person_positions, chair_positions = runModel(
        img)

    return jsonify({'status': 'success', 'person_count': person_count, 'chair_count': chair_count, 'person_positions': person_positions, 'chair_positions': chair_positions})

##################################################### THE REAL DEAL HAPPENS ABOVE ######################################


@app.route('/test', methods=['GET', 'POST'])
def test():
    print("log: got at test", file=sys.stderr)
    return jsonify({'status': 'succces'})


@app.route('/')
def home():
    return render_template('./index.html')


@app.after_request
def after_request(response):
    print("log: setting cors", file=sys.stderr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(debug=True)
