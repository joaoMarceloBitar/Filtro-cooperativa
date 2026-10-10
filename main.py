from reader import requests_parser
from processor import requests_filter

def main():
    build_aproved_requests_csv()

def build_aproved_requests_csv():
    requests = requests_parser()
    v = requests_filter(requests)
    for valid in v:
        print(valid) 

main()