import math
print('В команде Мастера кода участников: %(team1_num)s' % {'team1_num': 5})
print('Итого сегодня в командах участников: %(team1_num)s, %(team2_num)s !' % {'team1_num': 5,'team2_num': 6})
print('Команда Волшебники данных решила задач: {score_2} !'.format(score_2='42'))
print('Волшебники данных решили задачи за {0} !'.format('18015.2 с'))
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}')
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
time_avg = round(time_avg, 1)
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')