import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

url = "../date/Uber.xlsx"
data = pd.read_excel(url, engine="openpyxl")

income_sum = data.groupby(
    "dispatching_base_number"
    )["trips"].sum()

plt.figure(figsize=(10, 6))

sns.set(style="whitegrid")
sns.boxplot(
    x="dispatching_base_number",
    y="trips",
    hue="type",
    data=data
)

plt.title("Доля поездок для разных классов такси")

plt.show()