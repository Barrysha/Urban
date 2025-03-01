import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "test_analyst.xlsx"
data = pd.read_excel(url, engine="openpyxl")

data['event_date'] = pd.to_datetime(data['event_date'], errors='coerce')
data['day_of_week'] = data['event_date'].dt.day_name(locale='ru_RU')

order_days = [
    'Понедельник', 'Вторник', 'Среда',
    'Четверг', 'Пятница', 'Суббота', 'Воскресенье'
]

# 1. Линейный график количества событий по дате
plt.figure(figsize=(10, 6))
sns.lineplot(x='event_date', y='event_id', data=data, marker='o')
plt.title('Количество событий по дате')
plt.xlabel('Дата события')
plt.ylabel('Идентификатор события')
plt.grid(True)
plt.show()

# 2. Столбчатая диаграмма количества мероприятий по группам
plt.figure(figsize=(10, 6))
sns.countplot(x='group_ids', data=data)
plt.title('Количество мероприятий по группам')
plt.xlabel('Идентификатор группы')
plt.ylabel('Количество мероприятий')
plt.grid(True)
plt.show()

# 3. Круговая диаграмма распределения мероприятий по учителям
plt.figure(figsize=(10, 6))
labels = data['teacher_ids'].value_counts().index.astype(str).values
sizes = data['teacher_ids'].value_counts().values
explode = [0.1 if i == max(sizes) else 0 for i in sizes]
colors = sns.color_palette('pastel')[0:len(sizes)]
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Распределение мероприятий по учителям')
plt.legend(labels, loc='best')
plt.show()

# 4. Тепловая карта посещаемости мероприятий
plt.figure(figsize=(10, 6))
heat_df = data.pivot_table(
    index='group_ids', 
    columns='teacher_ids', 
    values='attendance_id', 
    aggfunc='mean'
    )
sns.heatmap(heat_df, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title('Тепловая карта посещаемости мероприятий')
plt.xlabel('Учителя')
plt.ylabel('Группы')
plt.show()

# 5. Точечная диаграмма событий по дням недели
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.swarmplot(
    x='day_of_week', hue='day_of_week',
    y='event_id', data=data,
    order=order_days,
    palette="Set1",
    size=5,
    legend=False
)
plt.title('События по дням недели', fontsize=14)
plt.xlabel('День недели', fontsize=12)
plt.ylabel('Идентификатор события', fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(True)
plt.show()