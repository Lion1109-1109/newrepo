from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to my Flask app! Learning never stops. - Rohit...........Biratnagar.</h1>'

@app.route('/about')
def about():
    return '<h1>This is a simple web app built with Flask. Keep exploring...........Nepal.</h1>'

@app.route('/contact')
def contact():
    return '<h1>Contact me anytime. Believe in yourself...........Rohit.</h1>'

@app.route('/fun')
def fun():
    return '<h1>Coding is creative and fun. Keep smiling...........Kathmandu.</h1>'

app.run(host='0.0.0.0', port=7000)
