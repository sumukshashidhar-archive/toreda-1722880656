import plotly.express as px


def viz(df):
    fig = px.line(df, y='close')
    fig.show()