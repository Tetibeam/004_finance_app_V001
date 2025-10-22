import pandas as pd
import sqlite3
import os

def load_csv_to_db(filepath, db_path):
    df = pd.read_csv(filepath)
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    df.to_sql("assets", conn, if_exists="replace", index=False)
    conn.close()

def get_total_assets(db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT date, 資産タイプ, 資産額 FROM assets", conn)
    conn.close()
    pivot = df.pivot_table(index="date", columns="資産タイプ", values="資産額", aggfunc="sum")
    return pivot

