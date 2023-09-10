from flask import Flask, jsonify, request
from datetime import datetime
app = Flask(__name__)


@app.route('/api')
def your_endpoint():

    # Get the track and slack name
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    week_day = datetime.now().strftime("%A")
    t = datetime.utcnow().isoformat().split('.')[0]
    t = t + 'Z'
    github_file = "https://github.com/njogued/HNGx/blob/main/0-api_endpoint/flask_api.py"
    data = {
        "current_day": week_day,
        "github_file_url": github_file,
        "github_repo_url": "https://github.com/njogued/HNGx",
        "slack_name": slack_name,
        "utc_time": t,
        "track": track,
        "status_code": 200
    }
    response = jsonify(data)

    # Set the Content-Type header to indicate that you are sending JSON
    response.headers['Content-Type'] = 'application/json'

    return response, 200


if __name__ == '__main__':
    app.run()
