import csv
import json
import sys
from reader import requests_loader, requests_parser
from processor import requests_filter
from models import ProcessingSummary, Request
from log import LOG_PATH, log

def main():
    open(LOG_PATH, "w", encoding="utf-8").close()
    if build_approved_requests_csv():
        sys.exit(0)
    sys.exit(1)

def build_approved_requests_csv() -> bool:
    log("Início do processamento")
    summary = ProcessingSummary()

    try:
        raw_requests = requests_loader()
        summary.read = len(raw_requests)
        requests = requests_parser(raw_requests)
        valid_requests = requests_filter(requests)
        build_csv(valid_requests)
        summary.exported = len(valid_requests)
        summary.ignored = summary.read - summary.exported
    except FileNotFoundError as error:
        log(f"erro: arquivo não encontrado: {error.filename}")
        return False
    except json.JSONDecodeError as error:
        log(f"erro: JSON inválido na linha {error.lineno}, coluna {error.colno}")
        return False
    except TypeError as error:
        log(f"erro: estrutura do JSON inválida: {error}")
        return False
    except OSError as error:
        log(f"erro: falha ao ler ou gravar arquivo: {error}")
        return False

    log(f"total de registros lidos: {summary.read}")
    log(f"total de registros exportados: {summary.exported}")
    log(f"total de registros ignorados: {summary.ignored}")
    log("fim do processamento")
    return True

def build_csv(requests: list[Request]):
    with open("aprovados.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["id", "nome", "cpf"])
        for r in requests:
            writer.writerow([r.id, r.nome, r.cpf])

main()
