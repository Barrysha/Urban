import plotly.graph_objects as go

# Данные
categories = [
    "Интерактивность", "Простота использования",
    "Визуальное оформление", "Производительность",
    "Настройка"
]

plotly_scores = [5, 5, 5, 2, 3]
seaborn_scores = [4, 4, 4, 1, 2]
matplot_scores = [3, 3, 3, 5, 5]

# Создание графика
fig = go.Figure()

# Добавление данных
fig.add_trace(go.Bar(
    y=categories,
    x=plotly_scores,
    name="Plotly",
    orientation="h",
    marker=dict(color="#1f77b4")
))

fig.add_trace(go.Bar(
    y=categories,
    x=seaborn_scores,
    name="Seaborn",
    orientation="h",
    marker=dict(color="#bcbd22")
))

fig.add_trace(go.Bar(
    y=categories,
    x=matplot_scores,
    name="Matplotlib",
    orientation="h",
    marker=dict(color="#d62728")
))

# Обновление макета

fig.update_layout(
    barmode="group",
    title="Сравнение библиотек по ключевым критериям",
    xaxis_title="Уровень",
    yaxis_title="Критерии",
    xaxis=dict(tickvals=[1, 2, 3, 4, 5], ticktext=['1', '2', '3', '4', '5']),
    template="plotly_white"
)

fig.show()