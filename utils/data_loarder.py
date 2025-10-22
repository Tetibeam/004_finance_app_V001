import pandas as pd
import sqlite3
import os

def load_csv_to_db(csv_files: list, db_path):
    """
    CSVファイルを読み込み、指定されたSQLiteデータベースに保存する。

    Args:
        csv_files (dict): テーブル名をキー、ファイルパスを値とする辞書。
        db_path (str): SQLiteデータベースのパス。

    """
    conn = sqlite3.connect(db_path)
    for table_name, file_path in csv_files.items():
        if not os.path.exists(file_path):
            print(f"⚠️ {file_path} が見つかりません。スキップします。")
            continue
        # ファイル名から拡張子を除いたものをテーブル名にする
        table_name = os.path.splitext(os.path.basename(file_path))[0]
        df = pd.read_csv(file_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"✅ {file_path} → テーブル '{table_name}' に登録しました。")

    conn.close()
    print("🎉 すべてのCSVを1つのDBに統合しました！")

def get_pivot_from_db(db_path: str, table_name: str,
                      index_col: str or list, columns_col: str or list, values_col: str or list,
                      aggfunc="sum", where_clause=None):
    conn = sqlite3.connect(db_path)
    query = f'SELECT * FROM "{table_name}"'
    if where_clause:
        query += f" WHERE {where_clause}"
    df = pd.read_sql_query(query, conn)
    conn.close()

    pivot = df.pivot_table(index=index_col, columns=columns_col, values=values_col, aggfunc=aggfunc)
    return pivot

