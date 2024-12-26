import matplotlib.pyplot as plt
import pandas as pd

url = "../date/Mall_Customers.xlsx"
data = pd.read_excel(url, engine="openpyxl")

ais = data.groupby("Genre")["Annual Income (k$)"].sum()

plt.pie(ais,
        labels=ais.index,
        autopct="%1.1f%%",
        colors=plt.cm.Paired.colors
)
plt.title("Доля ежегодного дохода для мужчин и женщин")

plt.show()