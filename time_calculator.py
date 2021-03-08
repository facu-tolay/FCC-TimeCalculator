def add_time(start, duration, day_week = ''):
    new_time = ''
    flag_optional = 0

    if day_week != '':
        flag_optional = 1
        day_week = day_week[0].upper() + day_week[1:].lower()
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        number_day = days_of_week.index(day_week)
    
    if duration == '0:00':
        if flag_optional != 1:
            return start
        else:
            return start + days_of_week[number_day]
    elif duration == '24:00':
        if flag_optional != 1:
            return start + ' (next day)'
        else:
            return start + ', ' + days_of_week[number_day + 1] + ' (next day)'
    
    time_format, clock_format = start.split(' ')
    hour, minute = time_format.split(':')
    hour_duration, minute_duration = duration.split(':')

    if clock_format == 'PM':
        n1 = int(hour) + int(hour_duration) + 12    
    else:
        n1 = int(hour) + int(hour_duration)
    n2 = int(minute) + int(minute_duration)

    if n2 > 60: n1 += 1

    n1 = n1 % 24 
    n2 %= 60

    if clock_format == 'AM' and (n1 >= 12 & n1 < 24):
        clock_format = 'PM'
    elif clock_format == 'PM' and (n1 >= 0 & n1 < 12):
        clock_format = 'AM'

    n1 %= 12

    if n1 == 0: n1 = 12
        
    if n2 < 10: n2 = str(0) + str(n2)

    if int(hour_duration)/24 >= 2:
        days =  int(int(hour_duration)/24) + 1
        if flag_optional != 1:
            new_time = str(n1) + ':' + str(n2) + ' '+ clock_format + ' (' + str(days) + ' days later)'
        else:
            new_time = str(n1) + ':' + str(n2) + ' '+ clock_format + ', ' + days_of_week[(number_day + days)%7]  + ' (' + str(days) + ' days later)'
    else:
        new_time = str(n1) + ':' + str(n2) + ' '+ clock_format
    
    return new_time