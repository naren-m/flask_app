from flask import Flask, render_template, Response
from camera import Video

from image_display import ImageDisplay

app = Flask(__name__)

imageObject = Video()

@app.route('/')
def hello_world():
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(imageObject),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/display')
def display():
    v = Video()
    v.display_video()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
    # display()
