import logging

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(f'Client IP: {request.remote_addr}')
    return jsonify({'ip': request.remote_addr}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
