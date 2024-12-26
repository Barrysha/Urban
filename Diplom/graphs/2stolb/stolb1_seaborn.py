import matplotlib.pyplot as plt
import pandas as pd
import  seaborn as sns

url = "../date/Mall_Customers.xlsx"
data = pd.read_excel(url, engine="openpyxl")

gender = data["Genre"]
ais = data.groupby("Genre")["Annual Income (k$)"].sum().reset_index()

sns.barplot(x="Genre",
            y="Annual Income (k$)",
            data=ais,
            color="#1f77b4"
)
plt.title('Годовой доход мужчин и женщин')
plt.xlabel('Пол покупателя')
plt.ylabel('Годовой доход покупателя')
plt.show()