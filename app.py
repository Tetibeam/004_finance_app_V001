from flask import Flask, render_template
from utils.data_loarder import get_total_assets
import pandas as pd
import plotly.express as px

DB_PATH_ASSET = "database/asset.db"
DB_PATH_BALANCE = "database/balance.db"
DB_PATH_TARGET = "database/target.db"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    pivot = get_total_assets(db_path=DB_PATH_ASSET).sum(axis=1)
    pivot_target = get_total_assets(db_path=DB_PATH_TARGET).sum(axis=1)
    df = pd.concat([pivot,pivot_target],axis=1, keys=["実績", "目標"])
    fig = px.line(df, x=df.index, y=df.columns, title="総資産推移", labels={"date": "日付", "value": "総資産","variable":""})
    graph_html = fig.to_html(full_html=False)
    return render_template("dashboard.html", graph_html=graph_html)

if __name__ == "__main__":
    app.run(debug=True)
