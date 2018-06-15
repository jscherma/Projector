from flask import Flask
from flask import Response

app = Flask(__name__)

# Example JSON output with a content-type header (via mimetype)
@app.route('/')
def hello_world():
    jsonBody = '{"examplePayload":1}'
    return Response(jsonBody, mimetype='text/json')
