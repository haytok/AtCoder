day = input()

print(0 if day == 'Saturday' or day == 'Sunday' else 5 - ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'].index(day))
