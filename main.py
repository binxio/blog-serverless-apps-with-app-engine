# [START gae_python37_app]
from flask import Flask, jsonify
from flask_basicauth import BasicAuth

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'user'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(app)

actors = [
    {'id': 1, 'actor': 'William Shatner', 'role': 'James T'},
    {'id': 2, 'actor': 'Leonard Nimoy', 'role': 'Spock'},
    {'id': 3, 'actor': 'DeForest Kelley', 'role': 'Leonard McCoy'},
    {'id': 4, 'actor': 'James Doohan', 'role': 'Montgomery Scott'},
    {'id': 5, 'actor': 'George Takei', 'role': 'Hikaru Sulu'},
    {'id': 6, 'actor': 'Walter Koenig', 'role': 'Pavel Chekov'},
    {'id': 7, 'actor': 'Nichelle Nichols', 'role': 'Nyota Uhura'},
    {'id': 8, 'actor': 'Majel Barrett', 'role': 'Christine Chapel'}
]

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/actors', methods=['GET'])
def get_persons():
    return jsonify(actors), 200

@app.route('/actors/<int:id>', methods=['GET'])
def get_actor_by_id(id: int):
    found = None
    for actor in actors:
        if actor['id'] == id:
            found = actor
            break

    if found:
        return jsonify(found), 200
    else:
        return '', 404

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]