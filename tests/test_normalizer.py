import pytest

from models import Status
from normalizer import normalize_cpf, normalize_id, normalize_request, normalize_status

def test_valid_record_is_normalized():
    record = {"id": 1, "nome": " Maria Silva ", "cpf": "123.456.789-00", "status": "aprovado"}

    result = normalize_request(record)

    assert result == {
        "id": "1",
        "nome": "Maria Silva",
        "cpf": "12345678900",
        "status": Status.APROVADO,
    }

def test_record_with_missing_field_is_rejected():
    record = {"id": 1, "nome": "Maria Silva", "status": "APROVADO"}

    with pytest.raises(ValueError):
        normalize_request(record)

def test_boolean_id_is_rejected():
    with pytest.raises(ValueError):
        normalize_id(True)

def test_null_cpf_becomes_empty_text():
    assert normalize_cpf(None) == ""

def test_numeric_cpf_is_rejected():
    with pytest.raises(ValueError):
        normalize_cpf(12345678900)

def test_cpf_with_less_than_11_digits_is_rejected():
    with pytest.raises(ValueError):
        normalize_cpf("123")

def test_unknown_status_is_rejected():
    with pytest.raises(ValueError):
        normalize_status("CANCELADO")
