import itertools
from operator import itemgetter

def ordered_list(args, data):
    output = []
    sorted_by = args['order_by'] if 'order_by' in args else 'datetime'
    lat = args['lat'] if 'lat' in args else 0
    lon = args['lon'] if 'lon' in args else 0
    start = int(args['start']) if 'start' in args else 0
    stop = int(args['stop']) if 'stop' in args else len(data)

    if sorted_by in data[0].keys():
        events = sorted(data, key=itemgetter(sorted_by))
    else:
        events = sorted(data, key=itemgetter('datetime'))
    if float(lat)>0 and float(lon) >0:
        for item in events:
            location = item['location'].split(',')
            if location[0] == float(lat) and location[1] == float(lon):
                output.append(item)
    else:
        output.append(events)
    return output[0][start:stop]
