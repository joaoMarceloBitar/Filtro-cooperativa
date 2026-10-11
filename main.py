from reader import requests_parser
from processor import requests_filter
from models import Request
import csv

def main():
    build_aproved_requests_csv()

def build_aproved_requests_csv():
    requests = requests_parser()
    v = requests_filter(requests)
    for valid in v:
        print(valid) 
    build_csv(v)

def build_csv(requests: Request):
    with open("soliciacoes_aprovadas","w",encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["id", "nome", "cpf"])
        for r in requests:
            writer.writerow([r.id,r.nome,r.cpf,r.status]) 


main()