from flask import Flask, url_for, redirect
from motorControl import MotorsAction, movement

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='RobotControl.html'))


@app.route('/forward')
def forward():
    movement(MotorsAction.Forward)
    return "forward"

@app.route('/reverse')
def reverse():
    movement(MotorsAction.Reverse)
    return 'reverse'


@app.route('/left')
def left():
    movement(MotorsAction.Left)
    return 'left'


@app.route('/right')
def right():
    movement(MotorsAction.Right)
    return 'right'


@app.route('/stop')
def stop():
    movement(MotorsAction.Stop)
    return 'stop'


@app.route('/clear')
def clear():
    movement(MotorsAction.Clear)
    return 'clear'


@app.route('/rotateright')
def rotateright():
    movement(MotorsAction.RotateRight)
    return 'rotateright'


@app.route('/rotateleft')
def rotateleft():
    movement(MotorsAction.RotateLeft)
    return 'rotateleft'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
