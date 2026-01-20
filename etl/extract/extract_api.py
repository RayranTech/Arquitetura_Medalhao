import requests
import json
from datetime import datetime
from pathlib import Path


BASE_URL = "https://fakestoreapi.com"
BRONZE_PATH = Path("data/bronze/api")
TIMEOUT = 30


def fetch_data(endpoint: str) -> list:
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


def save_raw_data(data: list, entity: str) -> None:
    BRONZE_PATH.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = BRONZE_PATH / f"{entity}_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def extract_entity(entity: str) -> None:
    data = fetch_data(entity)
    save_raw_data(data, entity)
    print(f"✅ {entity} extraído com sucesso!")


def main():
    entities = ["products", "carts"]

    for entity in entities:
        extract_entity(entity)


if __name__ == "__main__":
    main()
