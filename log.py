from datetime import datetime

LOG_PATH = "processamento.log"

def log(message: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} | {message}"
    print(line)
    with open(LOG_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(line + "\n")
