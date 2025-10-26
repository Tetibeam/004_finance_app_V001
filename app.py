from flask import Flask, render_template
from utils.read_from_db import get_asset_and_profit_dashboard, get_balance_dashboard
from utils.config import load_settings
import utils.visualize_dashboard as viz
from utils.calculation import cal_general_special_balance_dashboard,cal_total_return_target_dashboard
import os


settings = load_settings("setting.yaml")
DB_PATH_FINANCE = os.path.join(    settings["database_path"],"",settings["database"]["finance"])

app = Flask(__name__)

@app.route("/")
def index():
    # ダッシュボードがトップ
    return dashboard()

@app.route("/dashboard")
def dashboard():
    graphs = {}

    df_asset_profit = get_asset_and_profit_dashboard(DB_PATH_FINANCE) # DBから資産データを取得、整形
    df_asset_profit = cal_total_return_target_dashboard(df_asset_profit)

    # 1. 総資産推移
    fig = viz.display_total_assets(df_asset_profit)
    graphs["assets"] = viz.write_html(fig)

    # 2. トータルリターン推移
    fig = viz.display_total_returns(df_asset_profit)
    graphs["returns"]  = viz.write_html(fig)

    df_balance = get_balance_dashboard(DB_PATH_FINANCE)
    df_general = cal_general_special_balance_dashboard(df_balance, "一般収支")
    df_special = cal_general_special_balance_dashboard(df_balance, "特別収支")

    # 3. 一般収入・支出
    fig = viz.display_general_income_expenditure(df_general)
    graphs["general_income_expenditure"] = viz.write_html(fig)

    # 4. 一般収支
    fig = viz.display_general_balance(df_general)
    graphs["general_balance"]  = viz.write_html(fig)

    # 5. 特別収入・支出
    fig = viz.display_special_income_expenditure(df_special)
    graphs["special_income_expenditure"]  = viz.write_html(fig)

    # 6. 特別収支
    fig = viz.display_special_balance(df_special)
    #graphs["special_balance"] = fig.to_html(full_html=False)
    graphs["special_balance"]  = viz.write_html(fig)

    return render_template("dashboard.html", graphs=graphs)

if __name__ == "__main__":
    app.run(debug=True)
