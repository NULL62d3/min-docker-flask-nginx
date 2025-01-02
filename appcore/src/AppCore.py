from flask import Flask

app = Flask(__name__)

@app.route('/AppCore/sayHello', methods=['GET'])
def sayHello():
    return f"sayHello: Hello!"

@app.route('/AppCore/sayName/<name>', methods=['GET'])
def sayName(name):
    return f"sayName: Hello! {name}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)

