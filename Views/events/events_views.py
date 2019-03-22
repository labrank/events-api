from flask import jsonify, request, Blueprint, abort, request
import itertools
from operator import itemgetter

from controller import data
from Views.commons import ordered_list

events = Blueprint('events', __name__)

@events.route('/events', methods=['GET'])
def get_events():
    output = ordered_list(request.args, data.data)
    return jsonify({"events": output})

@events.route('/events/<string:uuid>', methods=['GET'])
def get_event(uuid):
    output = []
    try:
        find_one = next(item for item in data.data if item["uuid"] == uuid)
    except:
        abort(404)
    output.append(find_one)
    return jsonify({"events": output})
