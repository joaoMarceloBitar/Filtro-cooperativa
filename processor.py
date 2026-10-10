from models import Request

def requests_filter(requests: Request):
    valid_requests = [r for r in requests if r.status == "APROVADO" and r.cpf]
    return valid_requests
