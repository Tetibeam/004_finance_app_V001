from flask import Flask, render_template
import utils.data_visualize as dv
import yaml
import pandas as pd
import plotly.express as px
import utils.config as cfg

#DB_PATH_ASSET = "database/asset.db"
#DB_PATH_BALANCE = "database/balance.db"
#DB_PATH_TARGET = "database/target.db"

settings = cfg.load_settings("setting.yaml")

app = Flask(__name__)

@app.route("/")
def index():
    # 今回はダッシュボードがトップ
    return dashboard()

@app.route("/dashboard")
def dashboard():
    # 1. 総資産推移
    # 2. トータルリターン推移
    # 3. 任意グラフ（後で追加可能）
    # 4. 一般収支推移
    # 5. 特別収支推移
    # 6. 任意グラフ（後で追加可能）
    
    return render_template("dashboard.html", graphs=graphs)
    """
    pivot = get_total_assets(db_path=DB_PATH_ASSET).sum(axis=1)
    pivot_target = get_total_assets(db_path=DB_PATH_TARGET).sum(axis=1)
    df = pd.concat([pivot,pivot_target],axis=1, keys=["実績", "目標"])
    fig = px.line(df, x=df.index, y=df.columns, title="総資産推移", labels={"date": "日付", "value": "総資産","variable":""},template="plotly_dark")
    fig.update_xaxes(tickformat="%y/%m/%d")
    fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=35, b=40)  # 余白調整
    )
    graph_html = fig.to_html(full_html=False)
    return render_template("dashboard.html", graph_html=graph_html)
    """
if __name__ == "__main__":
    app.run(debug=True)
