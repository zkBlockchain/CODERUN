def generate_calendars(days_num, weekday):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    first_day_index = weekdays.index(weekday)

    days = list(range(1, days_num + 1))
    days = ['..'] * first_day_index + days
    weeks = [days[i:i + 7] for i in range(0, len(days), 7)]

    if len(weeks[-1]) < 7:
        weeks[-1] += ['..'] * (7 - len(weeks[-1]))
    
    flags = False
    for week in weeks:
        week_formats = []
        for day in week:
            if day != '..':
                day_format = '.{}' if len(str(day)) == 1 else '{:2}'
                week_formats.append(day_format.format(day))
            else:
                if not flags:
                    week_formats.append(day)
            if (day == days_num): 
                flags = True 
        print(' '.join(week_formats))


def main():
    days_num, weekday = input().split()
    generate_calendars(int(days_num), weekday)


if __name__ == '__main__':
    main()

