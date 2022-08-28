import calendar

input = input()
date = input.split('.')
weekdays = ['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai']

calendar = calendar.Calendar()
weekcalendar = calendar.monthdayscalendar(int(date[2]), int(date[1]))

for i in range (len(weekcalendar)):
    for j in range (len(weekcalendar[i])):
        week = weekcalendar[i]
        if week[j] == int(date[0]):
            weekday = weekdays[j]
            break

print(weekday)
