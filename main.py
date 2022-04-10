from flask import Flask, render_template
import subprocess
import sys
app=Flask(__name__)
app.debug = True  #  to activate debug mode 
# static routing
@app.route('/cartoonify')
def cartoonify():
    return str(subprocess.call(["python","./Cartoonify/cartoonifier-python-project.py"
]))

@app.route('/color_detection')
def color_detection():
    return str(subprocess.call(["python","./Color_detection/color_detection.py","-i","./Color_detection/colorpic.jpg"
]))

@app.route('/face_detection')
def face_detection():
    return str(subprocess.call(["python","./FaceDetection/Face.py"
]))

@app.route('/face_recognition')
def face_recognition():
    return f"""
    <a href="/facematch">Facematch</a><br>
    <a href="/findfaces">Findfaces</a><br>
    <a href="/identify">Identify</a><br>
    <a href="/pullfaces">Pull faces</a><br>
    """
@app.route('/facematch')
def face_match():
    return str(subprocess.call(["python","./Face_recognition_examples/facematch.py"
]))

@app.route('/findfaces')
def find_faces():
    return str(subprocess.call(["python","./Face_recognition_examples/findfaces.py"
]))

@app.route('/identify')
def identify():
    return str(subprocess.call(["python","./Face_recognition_examples/identify.py"
]))

@app.route('/pullfaces')
def pullfaces():
    return str(subprocess.call(["python","./Face_recognition_examples/pullfaces.py"
]))

@app.route('/foreground_detection')
def foreground_detection():
    return str(subprocess.call(["python","./Foreground_detection/foreground_detection.py"
]))

@app.route('/mask_detection')
def mask_detection():
    return str(subprocess.call(["python","./Real_Time_Face_Mask_Detection/main.py"
]))

@app.route('/webcam')
def webcam():
    return str(subprocess.call(["python","./Webcam_Paint_OpenCV/Webcam_Paint_OpenCV.py"
]))

@app.route('/')
def intro():
    return f"""
    <a href="/cartoonify">Cartoonify</a><br>
    <a href="/color_detection">Color detection</a><br>
    <a href="/face_detection">Face Detection</a><br>
    <a href="/face_recognition">Face Recognition examples</a><br>
    <a href="/foreground_detection">Foreground detection</a><br>
    <a href="/mask_detection">Real Time Face Mask detection</a><br>
    <a href="/webcam">Webcam Paint OpenCV</a><br>
    """
app.run(host='127.0.0.1', port=8080)