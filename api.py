from flask import Flask
from flask_restful import Resource, Api
from Views.events.events_views import events
from flask import jsonify

app = Flask(__name__)
api = Api(app)

app.register_blueprint(events)

@app.route('/', methods=['GET'])
def add_sales():
    return jsonify("Hello, events!")

if __name__ == '__main__':
    app.run(debug=True)
