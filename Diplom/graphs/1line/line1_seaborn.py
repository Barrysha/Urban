import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

url = "../date/Mall_Customers.xlsx"
data = pd.read_excel(url, engine="openpyxl")

customer_ID = data["CustomerID"]
date = data["Date"]

sns.lineplot(x=customer_ID, y=date)

plt.title('Регистрация покупателей по датам с Seaborn')
plt.xlabel('ID Покупателя')
plt.ylabel('Дата регистрации')

plt.show()