from models import Request, Status
from processor import filter_by_cpf, filter_by_status, requests_filter

def test_status_filter_keeps_only_approved():
    approved = Request(id="1", nome="Maria", cpf="12345678900", status=Status.APROVADO)
    pending = Request(id="2", nome="Ana", cpf="98765432100", status=Status.PENDENTE)

    result = filter_by_status([approved, pending])

    assert result == [approved]

def test_cpf_filter_removes_empty_cpf():
    with_cpf = Request(id="1", nome="Maria", cpf="12345678900", status=Status.APROVADO)
    without_cpf = Request(id="2", nome="João", cpf="", status=Status.APROVADO)

    result = filter_by_cpf([with_cpf, without_cpf])

    assert result == [with_cpf]

def test_requests_filter_keeps_only_approved_with_cpf():
    valid = Request(id="1", nome="Maria", cpf="12345678900", status=Status.APROVADO)
    pending = Request(id="2", nome="Ana", cpf="98765432100", status=Status.PENDENTE)
    without_cpf = Request(id="3", nome="João", cpf="", status=Status.APROVADO)

    result = requests_filter([valid, pending, without_cpf])

    assert result == [valid]
