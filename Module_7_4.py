team_1 = 'Мастера кода'
team_2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %:

print('В команде %s участников: %s!' % (team_1, team1_num))
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))

# Использование format():

print('Команда {0} решила задач: {1}'.format(team_2,score_2))
print('{0} решили задачи за {1} c'.format(team_2, team2_time))

# Использование f-строк:

print(f'Команды решили {score_1} и {score_2} задач.')

def challenge_result():
    if team1_time/score_1 > team2_time/score_2:
        print(f'Победа команды {team_1}!')
    if team1_time/score_1 == team2_time/score_2:
        print(f'Команды {team_1} и {team_2} набрали одинаковое количество баллов. Ничья!')
    else:
        print(f'Победа команды {team_2}!')

challenge_result()

print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")
