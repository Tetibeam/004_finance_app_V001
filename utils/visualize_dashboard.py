import plotly.express as px
import pandas as pd

def common_setting(fig):
    fig.update_xaxes(tickformat="%y/%m/%d")
    fig.update_layout(
        autosize=True,
        width=290,
        height=234,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0,r=0,t=50,b=20),
        title_font=dict(size=12),            # タイトル文字サイズ
        font=dict(size=8),                  # 軸ラベル・凡例などの共通サイズ
        legend=dict(
            visible=True,
            orientation="h",
            yanchor="bottom",
            y=1.1,
            xanchor="center",
            x=0.75,
            font=dict(size=8),
            #tracegroupgap=5,  # trace間のギャップ
        )
    )
    return fig

def display_total_assets(df):
    fig = px.line(
        df, x=df.index, y=["資産額_実績", "資産額_目標"],template="plotly_dark",title="総資産推移",
        labels={"date": "日付", "value":"資産額","variable":""}
        )
    fig = common_setting(fig)
    return fig

def display_total_returns(df):
    fig = px.line(df, x=df.index, y=["トータルリターン_実績", "トータルリターン_目標"],
              title="トータルリターン推移", labels={"date": "日付", "value":"リターン額","variable":""}, template="plotly_dark")
    fig = common_setting(fig)
    return fig

def display_general_income_expenditure(df):
    fig = px.bar(
        df, x=df.index, y=["金額_収入", "金額_支出"],barmode='group', template='plotly_dark',
        labels={'value':'金額', 'date':'年月', 'variable':''}, title = "一般収入・支出")
    #fig.show()
    fig.add_scatter(
        x=df.index,
        y=df['目標_収入'],
        mode='lines+markers',
        name='目標_収入',
        line=dict(color='blue', width=2)
    )
    fig.add_scatter(
        x=df.index,
        y=df['目標_支出'],
        mode='lines+markers',
        name='目標_支出',
        line=dict(color='orange', width=2)
    )
    fig = common_setting(fig)
    return fig

def display_general_balance(df):
    # 4. 一般収支
    fig = px.bar(
        df, x=df.index, y=["金額_収支"], template='plotly_dark',
        labels={'value':'金額', 'date':'年月', 'variable':''}, title = "一般収支"
    )
    fig.add_scatter(
        x=df.index,
        y=df['目標_収支'],
        mode='lines+markers',
        name='目標_収支',
        line=dict(color='orange', width=2)
    )
    fig = common_setting(fig)
    return fig

def display_special_income_expenditure(df):
    fig = px.bar(
        df, x=df.index, y=["金額_収入", "金額_支出"],barmode='group', template='plotly_dark',
        labels={'value':'金額', 'date':'年月', 'variable':''}, title = "特別収入・支出")

    fig.add_scatter(
        x=df.index,
        y=df['目標_収入'],
        mode='lines+markers',
        name='目標_収入',
        line=dict(color='blue', width=2)
    )
    fig.add_scatter(
        x=df.index,
        y=df['目標_支出'],
        mode='lines+markers',
        name='目標_支出',
        line=dict(color='orange', width=2)
    )
    fig = common_setting(fig)
    return fig

def display_special_balance(df):
    fig = px.line(
        df, x=df.index, y=["金額_収支","目標_収支"], template='plotly_dark', markers=True,
        labels={'value':'金額', 'date':'年月', 'variable':''}, title = "特別収支"
    )
    fig = common_setting(fig)
    return fig

