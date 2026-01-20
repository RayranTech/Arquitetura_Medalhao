import pandas as pd
from pathlib import Path


GOLD_PATH = Path("data/gold")
EXCEL_PATH = Path("excel")
EXCEL_FILE = EXCEL_PATH / "modelo_vendas_analitico.xlsx"


def load_gold(name: str) -> pd.DataFrame:
    file_path = GOLD_PATH / f"{name}.csv"
    return pd.read_csv(file_path)


def export_to_excel(tables: dict) -> None:
    EXCEL_PATH.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl") as writer:
        for sheet_name, df in tables.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)


def main():
    tables = {
        "dim_product": load_gold("dim_product"),
        "dim_date": load_gold("dim_date"),
        "fact_sales": load_gold("fact_sales"),
    }

    export_to_excel(tables)


if __name__ == "__main__":
    main()
