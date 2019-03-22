from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify

from Views.events.events_views import events
from Views.reporters.reporters_views import reporters
from Views.types.types_views import type

app = Flask(__name__)
api = Api(app)

app.register_blueprint(events)
app.register_blueprint(reporters)
app.register_blueprint(type)

@app.route('/', methods=['GET'])
def hello_events():
    return jsonify("Hello, events!")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
