from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api')
def your_endpoint():

    # Get the track and slack name
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    response = jsonify(data)

    # Set the Content-Type header to indicate that you are sending JSON
    response.headers['Content-Type'] = 'application/json'

    return response, 200


if __name__ == '__main__':
    app.run()
