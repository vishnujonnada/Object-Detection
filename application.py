from flask import Flask, render_template, Response
from flask_bootstrap import Bootstrap

from object_detection import *
from camera_settings import *

application = Flask(__name__)
Bootstrap(application)

def load_video_streaming():
    try:
        return VideoStreaming()
    except cv2.error as e:
        print("Error loading YOLOv3 weights:", e)
        return None

check_settings()
VIDEO = load_video_streaming()

@application.route("/")
def home():
    TITLE = "Object detection"
    return render_template("index.html", TITLE=TITLE)

@application.route("/video_feed")
def video_feed():
    if VIDEO is None:
        return "Error: YOLOv3 weights not loaded!"
    return Response(VIDEO.show(), mimetype="multipart/x-mixed-replace; boundary=frame")

# Button requests with error handling
@application.route("/request_preview_switch")
def request_preview_switch():
    if VIDEO is None:
        return "Error: YOLOv3 weights not loaded!"
    VIDEO.preview = not VIDEO.preview
    print("*"*10, VIDEO.preview)
    return "nothing"

@application.route("/request_flipH_switch")
def request_flipH_switch():
    if VIDEO is None:
        return "Error: YOLOv3 weights not loaded!"
    VIDEO.flipH = not VIDEO.flipH
    print("*"*10, VIDEO.flipH)
    return "nothing"

@application.route("/request_model_switch")
def request_model_switch():
    if VIDEO is None:
        return "Error: YOLOv3 weights not loaded!"
    VIDEO.detect = not VIDEO.detect
    print("*"*10, VIDEO.detect)
    return "nothing"

@application.route("/request_exposure_down")
def request_exposure_down():
    if VIDEO is None:
        return "Error: YOLOv3 weights not loaded!"
    VIDEO.exposure -= 1
    print("*"*10, VIDEO.exposure)
    return "nothing"

@application.route("/request_exposure_up")
def request_exposure_up():
    if VIDEO is None:
        return "Error: YOLOv3 weights not loaded!"
    VIDEO.exposure += 1
    print("*"*10, VIDEO.exposure)
    return "nothing"

@application.route("/request_contrast_down")
def request_contrast_down():
    if VIDEO is None:
        return "Error: YOLOv3 weights not loaded!"
    VIDEO.contrast -= 4
    print("*"*10, VIDEO.contrast)
    return "nothing"

@application.route("/request_contrast_up")
def request_contrast_up():
    if VIDEO is None:
        return "Error: YOLOv3 weights not loaded!"
    VIDEO.contrast += 4
    print("*"*10, VIDEO.contrast)
    return "nothing"

@application.route("/reset_camera")
def reset_camera():
    if VIDEO is None:
        return "Error: YOLOv3 weights not loaded!"
    STATUS = reset_settings()
    print("*"*10, STATUS)
    return "nothing"

if __name__ == "__main__":
    application.run(debug=True)
