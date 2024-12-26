import plotly.express as px
import pandas as pd

url = "../date/Mall_Customers.xlsx"
data = pd.read_excel(url, engine="openpyxl")

ais = data.groupby("Genre")["Annual Income (k$)"].sum().reset_index()

fig = px.pie(
    ais,
    names="Genre",
    values="Annual Income (k$)",
    title="Доля дохода для мужчин и женщин с Plotly"
)
fig.show()