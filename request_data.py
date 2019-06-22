import collections
from flask import request
def get_payload():
    payload = collections.defaultdict()
    if len(request.data) > 10000000000:
        pass
    if request.args:
        for key in request.args.keys():
            if not payload.get(key):
                payload[key] = []
            payload[key].extend(request.args.getlist(key))
    if request.form:
        for key in request.form.keys():
            if not payload.get(key):
                payload[key] = []
            payload[key].extend(request.form.getlist(key))
    if request.files:
        payload['files'] = collections.defaultdict(list)
        for key in request.files.keys():
            payload['files'][key].extend(request.files.getlist(key))
    for key in payload.keys():
        if key != 'files':
            value = payload.get(key)
            if len(value) == 1:
                payload[key] = value[0]
    content_type = (request.headers.get('Content-Type') or '').split(';')[0].lower()
    if content_type == 'application/json':
        if request.data.strip():
            try:
                parsed_json = request.get_json()
                # if isinstance(parsed_json, list):
                #     raise InvalidInput(detail='JSON payload must be an object, not a list', pointer='/')
                payload.update(parsed_json)
            except Exception as e:
                return "Invalid Format"
    return payload