import matplotlib.pyplot as plt
import pandas as pd

url = "../date/Mall_Customers.xlsx"
data = pd.read_excel(url, engine="openpyxl")

gender = data["Genre"]
ais = data.groupby("Genre")["Annual Income (k$)"].sum().reset_index()

plt.bar(ais["Genre"], ais["Annual Income (k$)"])
plt.title('Годовой доход мужчин и женщин')
plt.xlabel('Пол покупателя')
plt.ylabel('Годовой доход')

plt.show()