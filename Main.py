from flask import Flask, jsonify, abort
app = Flask(__name__)

@app.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400

@app.route('/', methods=['GET'])
def hello():
    return jsonify(about='Hello, WP!')

@app.route('/oneadder/<num>', methods=['GET'])
def one_adder(num):
    try:
        input = (int) (num)
    except ValueError:
         abort(400, description='Received an invalid argument. Please enter an integer.')

    return jsonify({'result': 1 + input})

if __name__ == '__main__':
    app.run(debug=True)
