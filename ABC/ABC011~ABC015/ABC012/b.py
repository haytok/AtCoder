import datetime

time = int(input())

hour = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60 # N % 60 でもOK!

# datetime.time(hour, minutes, seconds) でもOK!
print(datetime.time(hour=hour, minute=minutes, second=seconds))
