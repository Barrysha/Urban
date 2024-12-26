import matplotlib.pyplot as plt
import pandas as pd

url = "../date/Mall_Customers.xlsx"
data = pd.read_excel(url, engine="openpyxl")

customer_ID = data["CustomerID"]
date = data["Date"]

plt.plot(customer_ID, date)

plt.title('Регистрация покупателей по датам с Matplotlib')
plt.xlabel('ID Покупателя')
plt.ylabel('Дата регистрации')

plt.show()