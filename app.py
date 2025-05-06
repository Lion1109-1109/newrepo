from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def add_numbers():
    num1 = request.args.get('num1', default=0, type=float)
    num2 = request.args.get('num2', default=0, type=float)
    total = num1 + num2
    return f'<h1>The sum of {num1} and {num2} is {total}...........Rohit.</h1>'

app.run(host='0.0.0.0', port=7000)
