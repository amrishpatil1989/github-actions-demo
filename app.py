from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'version': '1.0.0'})


@app.route('/square/<int:n>')
def square(n):
    return jsonify({'input': n, 'result': n * n})


@app.route('/greet/<name>')
def greet(name):
    return jsonify({'message': f'Hello, {name}!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)