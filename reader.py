import json
from models import Request

def requests_parser():
    requests_object = requests_loader()
    parsed_requests = []
    for request in requests_object:
        parsed_request = Request(**request)
        parsed_requests.append(parsed_request)
    return parsed_requests

def requests_loader():
    requests_path = "solicitacoes.json"
    with open(requests_path, "r", encoding="utf-8") as raw_requests:
        requests = json.load(raw_requests)
        return requests

