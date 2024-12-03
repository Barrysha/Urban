x = "Мастера кода"
y = "Волшебники данных"
team_MK = 5
team_VD = 6
score_MK = 40
score_VD = 42
team_MK_time = 1801.2
team_VD_time = 2002.1
task_total = score_MK + score_VD
time_avg = (team_MK_time + team_VD_time)/task_total
winer = x if score_MK > score_VD else y

print("В команде Мастера кода %d участников!" % team_MK, '\n')
print("Итого в командах %d и %d участников!" % (team_MK, team_VD), '\n')

print("Команда Волшебники данных решила {} задач!".format(score_VD), '\n')
print("Команда Мастера кода решила задачи за {} секунды!".format(team_MK_time), '\n')

print(f"команды решили {task_total} задачи! {score_MK} и {score_VD}!", '\n')

print(f"Победила команда {winer}!", '\n')

print(f"Сегодня было решено {task_total} задачи. Среднее время на решение - {round(time_avg, 2)} с!")
