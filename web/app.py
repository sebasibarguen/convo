import time

import flask
from flask import request, jsonify
from flask import render_template

from fuzzy_match import FuzzyMatcher
from .errors import InvalidParameters


app = flask.Flask(__name__)
matcher = FuzzyMatcher()


@app.errorhandler(InvalidParameters)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api', methods=['GET'])
def api():

    query_params = request.args

    if 'keyword' not in query_params:
        raise InvalidParameters(
            '<keyword> parameter is required', status_code=400)

    keyword = query_params['keyword']

    start = time.perf_counter()
    suggestions = matcher.match(keyword)
    end = time.perf_counter()

    response = {'ok': True, 'suggestions': suggestions,
                'time[s]': f'{end - start:0.4f}'}
    return jsonify(response)
