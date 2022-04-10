from flask import Flask, render_template
import subprocess
import sys
app=Flask('app')
app.debug = True  #  to activate debug mode 
# static routing
@app.route('/cartoonify')
def cartoonify():
    return str(subprocess.call(["python","../Cartoonify/cartoonifier-python-project.py"
]))

@app.route('/color_detection')
def color_detection():
    return str(subprocess.call(["python","../Color_detection/color_detection.py","-i","../Color_detection/colorpic.jpg"
]))

@app.route('/face_detection')
def face_detection():
    return str(subprocess.call(["python","../FaceDetection/Face.py"
]))

@app.route('/')
def intro():
    return f"""
    <a href="/cartoonify">Cartoonify</a><br>
    <a href="/color_detection">Color detection</a><br>
    <a href="/face_detection">Face Detection</a><br>
    """
app.run(host='0.0.0.0', port=8080)