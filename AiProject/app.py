from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import cv2
import numpy as np
#from model import api

app = Flask(__name__)
#CORS(app)  # Enable CORS for all routes
#api.init_app(app)

# Function to perform object detection using YOLO (replace this with your actual YOLO detection function)


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
