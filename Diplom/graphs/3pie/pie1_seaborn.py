import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

url = "../date/Mall_Customers.xlsx"
data = pd.read_excel(url, engine="openpyxl")

ais = data.groupby("Genre")["Annual Income (k$)"].sum()

sns.set(style="whitegrid")

plt.pie(ais,
        labels=ais.index,
        autopct="%1.1f%%",
        colors=sns.color_palette("Set2", len(ais))
)
plt.title("Доля ежегодного дохода для мужчин и женщин")

plt.show()