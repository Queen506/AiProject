from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np

app = Flask(__name__)

# Function to perform object detection using YOLO (replace this with your actual YOLO detection function)


def perform_object_detection(image):
    # Your object detection logic here
    # ...
    # Return the image with bounding boxes drawn
    # Here's an example using OpenCV to draw bounding boxes
    # Assuming objects_detected is a list of detected objects with format {'label': 'person', 'confidence': 0.85, 'bbox': {'xmin': 10, 'ymin': 20, 'xmax': 100, 'ymax': 200}}
    for obj in detect_objects():
        label = obj['label']
        confidence = obj['confidence']
        bbox = obj['bbox']
        xmin, ymin, xmax, ymax = bbox['xmin'], bbox['ymin'], bbox['xmax'], bbox['ymax']
        color = (0, 255, 0)  # Green color for bounding boxes
        # Draw bounding box rectangle on the image
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 2)
        # Put label and confidence above the bounding box
        text = f'{label}: {confidence:.2f}'
        cv2.putText(image, text, (xmin, ymin - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    return image


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detect', methods=['POST'])
def detect_objects():
    # Get the uploaded XML file and image file
    xml_file = request.files['xml_file']
    image_file = request.files['image_file']

    # Save the XML file to a temporary location
    xml_file_path = 'labeled.xml'
    xml_file.save(xml_file_path)

    # Read the image
    image = cv2.imdecode(np.frombuffer(
        image_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Perform object detection using YOLO (replace this with your actual YOLO detection function)
    image_with_boxes = perform_object_detection(image)

    # Save the image with bounding boxes to a temporary file
    # 'static' is a folder in your Flask app where you can store static files
    output_image_path = 'static/img/image5.jpg'
    cv2.imwrite(output_image_path, image_with_boxes)

    # Return the path to the saved image
    return jsonify({'image_path': output_image_path})


if __name__ == '__main__':
    app.run(debug=True)
