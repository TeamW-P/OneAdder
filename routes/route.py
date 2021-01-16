from flask import jsonify, abort, Blueprint
from core.Adder import Adder
from . import routes

@routes.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400

@routes.route('/<num>', methods=['GET'])
def one_adder(num):
    try:
        value = (int) (num)
    except ValueError:
        abort(400, description='Received an invalid argument. Please enter an integer.')

    return jsonify({'result': Adder.oneAdder(value)})