from flask import jsonify, request, Blueprint, abort
import itertools
from operator import itemgetter

from controller import data
from Views.commons import ordered_list

reporters = Blueprint('reporters', __name__)

@reporters.route('/reporters', methods=['GET'])
def get_events():
    output = {}
    events = []
    count = 0
    reporters = sorted(data.data, key=itemgetter('reporter'))
    for key, value in itertools.groupby(reporters, key=itemgetter('reporter')):
        for i in value:
            count +=1
            events.append(i.get('name'))
        output[key] = { **{'events':events}, **{'count':[count]}, **{'path': '/reporters/events/'+key}}
        count = 0
        events = []
    return jsonify({'reporters': output})

@reporters.route('/reporters/events/<string:name>', methods=['GET'])
def get_event(name):
    output = []
    info = ordered_list(request.args, data.data)
    for item in info:
        if item['reporter'] == name:
            output.append(item)
    return jsonify({'count':len(output),'Reporter':name,'events': output})
