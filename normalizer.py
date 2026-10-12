from models import Status

REQUIRED_FIELDS = {"id", "nome", "cpf", "status"}

def normalize_request(request: object):
    if not isinstance(request, dict):
        raise ValueError(f"o registro deve ser um objeto, mas é {type(request).__name__}")

    missing_fields = REQUIRED_FIELDS - request.keys()
    if missing_fields:
        raise ValueError(f"campos ausentes: {', '.join(sorted(missing_fields))}")
    extra_fields = request.keys() - REQUIRED_FIELDS
    if extra_fields:
        raise ValueError(f"campos inesperados: {', '.join(sorted(extra_fields))}")

    return {
        "id": normalize_id(request["id"]),
        "nome": normalize_nome(request["nome"]),
        "cpf": normalize_cpf(request["cpf"]),
        "status": normalize_status(request["status"]),
    }

def normalize_id(value: object):
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise ValueError(f"id deve ser número ou texto, mas é {type(value).__name__}")
    request_id = str(value).strip()
    if not request_id:
        raise ValueError("id vazio")
    return request_id

def normalize_nome(value: object):
    if not isinstance(value, str):
        raise ValueError(f"nome deve ser texto, mas é {type(value).__name__}")
    nome = value.strip()
    if not nome:
        raise ValueError("nome vazio")
    return nome

def normalize_cpf(value: object):
    if value is None:
        return ""
    if not isinstance(value, str):
        raise ValueError(f"cpf deve ser texto, mas é {type(value).__name__}")
    cpf = value.strip().replace(".", "").replace("-", "")
    if cpf and not (cpf.isdigit() and len(cpf) == 11):
        raise ValueError(f"cpf deve ter 11 dígitos: {value}")
    return cpf

def normalize_status(value: object):
    if not isinstance(value, str):
        raise ValueError(f"status deve ser texto, mas é {type(value).__name__}")
    status = value.strip().upper()
    if status not in Status.__members__:
        raise ValueError(f"status desconhecido: {value}")
    return Status(status)
