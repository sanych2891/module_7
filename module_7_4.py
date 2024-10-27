team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = 'Победа команды "Мастера кода!"'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'Победа команды "Волшебники Данных!"'
else:
    challenge_result = 'Ничья!'

#Использование '%'
result_Masters = "В команде 'Мастера кода' участников: %.f !" % team1_num
result_Wizards = "В команде 'Волшебники данных': %.f !" % team2_num
result = "Итого сегодня в командах участников: %.f и %.f" % (team1_num, team2_num)

#Использование format()
result1 = "Команда 'Мастера кода' решила задач {} !".format(score1)
result2 = "Команда 'Волшебники данныйх' решила задач {} !".format(score2)

#Использование f-строк
result3 = f"Команды решили {score1} и {score2} задач!"
result4 = f"Результат битвы: {challenge_result}"
result5 = f"Сегодня было решено {tasks_total} задач в среднем по {time_avg:.1f} секунд на задачу"

#Запись в файл
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(result_Masters + '\n')
    f.write(result_Wizards + '\n')
    f.write(result + '\n')
    f.write(result1 + '\n')
    f.write(result2 + '\n')
    f.write(result3 + '\n')
    f.write(result4 + '\n')
    f.write(result5 + '\n')
