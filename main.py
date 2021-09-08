from flask import Flask, jsonify,request, render_template
import helpers

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

BASE_URL = 'https://swapi.dev/api/'

@app.route("/character/<name>/")
def get_character(name):
    all_details = helpers.getCharacterPlanetInfo(name)
    return jsonify(all_details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

