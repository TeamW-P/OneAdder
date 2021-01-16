from flask import Flask, jsonify
from routes import *

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/', methods=['GET'])
def hello():
    return jsonify(about='Hello, WP!')

if __name__ == '__main__':
    app.run(debug=True)