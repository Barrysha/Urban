import plotly.figure_factory as ff
import pandas as pd

url = "../date/Uber.xlsx"

data = pd.read_excel(url, engine="openpyxl")

columns = [
    'dispatching_base_number',
    'type', 'active_vehicles',
    'trips'
]

fig = ff.create_scatterplotmatrix(
    data[columns],
    diag='histogram',
    index='type',
    title='Матрица рассеяния параметров Uber',
    height=1000,
    width=1200
)

fig.update_layout(
    xaxis_title='dispatching_base_number',
    yaxis_title='trips',
    font=dict(size=14),
    plot_bgcolor='ghostwhite'
)

fig.show()