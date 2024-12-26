import matplotlib.pyplot as plt
import pandas as pd

url = "../date/Uber.xlsx"
data = pd.read_excel(url, engine="openpyxl")

x = data['active_vehicles']
y = data['trips']
categories = data['type'].unique().tolist()

colors = {
    'econom': 'b',  # синий
    'business': 'g',  # зеленый
    'premier': 'r',  # красный
    'elite': 'c',  # голубой
}

fig, ax = plt.subplots()

for cat in categories:
    indices = data['type'] == cat
    ax.scatter(
        x[indices],
        y[indices],
        c=colors[cat],
        label=cat,
        alpha=0.7  # Прозрачность точек
    )

ax.legend()

ax.set_xlabel('active_vehicles')
ax.set_ylabel('trips')

ax.set_title('Точечный график')

plt.show()