from flask import Flask, render_template
from utils.data_loarder import get_total_assets
import plotly.express as px

DB_PATH_ASSET = "database/asset.db"
DB_PATH_BALANCE = "database/balance.db"
DB_PATH_TARGE = "database/target.db"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    pivot = get_total_assets(db_path=DB_PATH_ASSET)
    df = pivot.sum(axis=1)
    fig = px.line(df, x=df.index, y=df.values, title="総資産推移", labels={"x": "日付", "y": "総資産"})
    fig.update_layout(xaxis_rangeslider_visible=True)
    graph_html = fig.to_html(full_html=False)
    return render_template("dashboard.html", graph_html=graph_html)

if __name__ == "__main__":
    app.run(debug=True)
