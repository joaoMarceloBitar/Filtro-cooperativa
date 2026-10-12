import json
from models import Request
from normalizer import normalize_request
from log import log

def requests_parser(requests: list):
    parsed_requests = []
    for request in requests:
        try:
            parsed_request = Request(**normalize_request(request))
        except ValueError as error:
            log(f"registro ignorado (dado bruto inválido): {request}, {error}")
            continue
        parsed_requests.append(parsed_request)
    return parsed_requests

def requests_loader():
    requests_path = "solicitacoes.json"
    with open(requests_path, "r", encoding="utf-8") as raw_requests:
        requests = json.load(raw_requests)
    if not isinstance(requests, list):
        raise TypeError(f"o JSON deve conter uma lista de registros, mas contém {type(requests).__name__}")
    return requests
