from models import  Status
from log import log

def requests_filter(requests: list):
    approved_requests = filter_by_status(requests)
    return filter_by_cpf(approved_requests)

def filter_by_status(requests: list):
    approved_requests = []
    for r in requests:
        if r.status != Status.APROVADO:
            log(f"registro ignorado: id={r.id} (status {r.status})")
            continue
        approved_requests.append(r)
    return approved_requests

def filter_by_cpf(requests: list):
    requests_with_cpf = []
    for r in requests:
        if not r.cpf:
            log(f"registro ignorado: id={r.id} (CPF vazio)")
            continue
        requests_with_cpf.append(r)
    return requests_with_cpf
