import json
import requests


def jarvis(email):
    jarvis_enpoint = {LINK TO THE HOSTED END POINT}

    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'email':email
    }
    result = requests.post(jarvis_enpoint, headers=headers, data=json.dumps(payload))
    result = json.loads((result.text))
    return result
