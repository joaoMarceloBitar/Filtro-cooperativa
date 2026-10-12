from models import Request, Status
from log import log

def requests_filter(requests: list[Request]) -> list[Request]:
    valid_requests = []
    for r in requests:
        if r.status != Status.APROVADO:
            log(f"registro ignorado: id={r.id} (status {r.status})")
            continue
        if not r.cpf:
            log(f"registro ignorado: id={r.id} (CPF vazio)")
            continue
        valid_requests.append(r)
    return valid_requests
