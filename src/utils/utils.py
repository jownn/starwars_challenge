import json
from flask import Response

def get_json_response(data):
    return Response(json.dumps(data, default=str), mimetype="application/json")
