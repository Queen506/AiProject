import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
import cv2
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

model = load_model("yolov3_custom.h5")

height = 224
width = 224



#api endpoint
@api.route("/predict")
class predict_image(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('image', type=str, required=True, help='Image path')
        args = parser.parse_args()

        img_path = args['image']
        img = image.load_img(img_path, target_size=(height, width))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array)

        return {'predictions': predictions.tolist()}

'''
#http request
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(height, width)) #loadไฟล์รูปภาพ
    img_array = image.img_to_array(img) #แปลงรูปภาพในรูปแบบ PIL (Pillow) เป็น NumPy array
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)

    return predictions

image_path = "static/img/image5.jpg"
image = cv2.imread(image_path)


predictions = predict_image(image_path)
'''
