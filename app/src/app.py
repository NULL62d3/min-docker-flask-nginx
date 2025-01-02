from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route('/<name>')
def hello(name):
    return f"hello! {name}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)