#!/usr/bin/env python

import os
import simplejson
from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open('static/releases.json') as f:
            contents = f.read()
        return Response(response=contents, mimetype='application/json')
    except IOError:
        return Response('No results (yet)')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
