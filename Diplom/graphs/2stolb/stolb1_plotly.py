import plotly.express as px
import pandas as pd

url = "../date/Mall_Customers.xlsx"
data = pd.read_excel(url, engine="openpyxl")

gender = data["Genre"]
ais = data.groupby("Genre")["Annual Income (k$)"].sum().reset_index()

fig = px.bar(data,
             x="Genre",
             y="Annual Income (k$)",
             color="Annual Income (k$)",
             title="Годовой доход мужчин и женщин",
             labels={"Пол": gender,
                     "Годовой доход": ais
             }
)
fig.show()