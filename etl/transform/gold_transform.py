import pandas as pd
from pathlib import Path


SILVER_PATH = Path("data/silver")
GOLD_PATH = Path("data/gold")


def load_silver(name: str) -> pd.DataFrame:
    file_path = SILVER_PATH / f"{name}.csv"
    return pd.read_csv(file_path)


def create_dim_product(df_products: pd.DataFrame) -> pd.DataFrame:
    dim_product = df_products[[
        "product_id",
        "product_name",
        "category",
        "price"
    ]].drop_duplicates()

    return dim_product


def create_dim_date(df_sales: pd.DataFrame) -> pd.DataFrame:
    dim_date = df_sales[["date"]].drop_duplicates()
    dim_date["date"] = pd.to_datetime(dim_date["date"])

    dim_date["year"] = dim_date["date"].dt.year
    dim_date["month"] = dim_date["date"].dt.month
    dim_date["month_name"] = dim_date["date"].dt.month_name()
    dim_date["day"] = dim_date["date"].dt.day

    return dim_date


def create_fact_sales(
    df_sales: pd.DataFrame,
    df_products: pd.DataFrame
) -> pd.DataFrame:

    fact = df_sales.merge(
        df_products,
        on="product_id",
        how="left"
    )

    fact["total_value"] = fact["quantity"] * fact["price"]

    fact = fact[[
        "cart_id",
        "product_id",
        "date",
        "quantity",
        "price",
        "total_value"
    ]]

    return fact


def save_gold(df: pd.DataFrame, name: str) -> None:
    GOLD_PATH.mkdir(parents=True, exist_ok=True)
    file_path = GOLD_PATH / f"{name}.csv"
    df.to_csv(file_path, index=False)


def main():
    df_products = load_silver("silver_products")
    df_sales = load_silver("silver_sales")

    dim_product = create_dim_product(df_products)
    dim_date = create_dim_date(df_sales)
    fact_sales = create_fact_sales(df_sales, df_products)

    save_gold(dim_product, "dim_product")
    save_gold(dim_date, "dim_date")
    save_gold(fact_sales, "fact_sales")


if __name__ == "__main__":
    main()
