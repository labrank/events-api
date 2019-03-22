from flask import jsonify, request, Blueprint, request
import itertools
from operator import itemgetter

from controller import data
from Views.commons import ordered_list

type = Blueprint('type', __name__)

@type.route('/types', methods=['GET'])
def get_events():
    output = {}
    types = []
    count = 0
    type = sorted(data.data, key=itemgetter('type'))
    for key, value in itertools.groupby(type, key=itemgetter('type')):
        for i in value:
            count +=1
        output[key] = {**{'count':count}, **{'path': '/types/events/'+ key}}
        count = 0
        events = []
    return jsonify({'Types': output})

@type.route('/types/events/<string:type>', methods=['GET'])
def get_event(type):
    output = []
    info = ordered_list(request.args, data.data)
    for item in info:
        if item['type'] == type:
            output.append(item)
    return jsonify({'Total':len(output),'events': output})
