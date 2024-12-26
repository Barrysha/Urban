import plotly.graph_objects as go
import pandas as pd

url = "../date/Mall_Customers.xlsx"
data = pd.read_excel(url, engine="openpyxl")

customer_ID = data["CustomerID"]
date = data["Date"]

fig = go.Figure(data=go.Scatter(
    x=customer_ID,
    y=date,
    mode="markers")
)
fig.update_layout(
    title="Регистрация покупателей по датам с Plotly",
    xaxis_title="ID Покупателя",
    yaxis_title="Дата регистрации"
)

fig.show()