import json
from dataclasses import replace
from models import Request
from log import log

def requests_parser(requests: list):
    parsed_requests = []
    for request in requests:
        try:
            parsed_request = Request(**request)
        except TypeError as error:
            log(f"registro ignorado (dado bruto inválido): {request}, {error}")
            continue
        parsed_request = replace(parsed_request, id=str(parsed_request.id))
        parsed_requests.append(parsed_request)
    return parsed_requests

def requests_loader():
    requests_path = "solicitacoes.json"
    with open(requests_path, "r", encoding="utf-8") as raw_requests:
        requests = json.load(raw_requests) 
        return requests
