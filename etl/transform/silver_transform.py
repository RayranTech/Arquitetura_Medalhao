import json
import pandas as pd
from pathlib import Path


BRONZE_PATH = Path("data/bronze/api")
SILVER_PATH = Path("data/silver")


def get_latest_file(entity: str) -> Path:
    files = sorted(BRONZE_PATH.glob(f"{entity}_*.json"))
    if not files:
        raise FileNotFoundError(f"Nenhum arquivo encontrado para {entity}")
    return files[-1]


def load_json(file_path: Path) -> list:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def transform_products(data: list) -> pd.DataFrame:
    df = pd.json_normalize(data)

    df = df.rename(columns={
        "id": "product_id",
        "title": "product_name",
        "price": "price",
        "category": "category",
        "rating.rate": "rating_rate",
        "rating.count": "rating_count"
    })

    return df


def transform_carts(data: list) -> pd.DataFrame:
    records = []

    for cart in data:
        for product in cart["products"]:
            records.append({
                "cart_id": cart["id"],
                "user_id": cart["userId"],
                "date": cart["date"],
                "product_id": product["productId"],
                "quantity": product["quantity"]
            })

    df = pd.DataFrame(records)
    df["date"] = pd.to_datetime(df["date"])

    return df


def save_silver(df: pd.DataFrame, name: str) -> None:
    SILVER_PATH.mkdir(parents=True, exist_ok=True)
    file_path = SILVER_PATH / f"{name}.csv"
    df.to_csv(file_path, index=False)


def main():
    products_file = get_latest_file("products")
    carts_file = get_latest_file("carts")

    products_data = load_json(products_file)
    carts_data = load_json(carts_file)

    df_products = transform_products(products_data)
    df_sales = transform_carts(carts_data)

    save_silver(df_products, "silver_products")
    save_silver(df_sales, "silver_sales")


if __name__ == "__main__":
    main()
