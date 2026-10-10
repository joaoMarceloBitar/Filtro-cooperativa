from dataclasses import dataclass
from enum import StrEnum

class Status(StrEnum):
    APROVADO = "APROVADO"
    PENDENTE = "PENDENTE"
    REPROVADO = "REPROVADO"

@dataclass(frozen=True)
class Request:
    id: str
    nome: str
    cpf: str
    status: Status