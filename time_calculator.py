def add_time(start, duration, day = ''):
  start_hour = int(start.replace(' AM', '').replace(' PM', '').split(':')[0])
  start_minute = int(start.replace(' AM', '').replace(' PM', '').split(':')[1])
  am_pm = start.split(' ')[1]
  duration_hour = int(duration.split(':')[0])
  duration_minute = int(duration.split(':')[1])
  next_day = 0

  new_hour = start_hour + duration_hour
  new_minute = start_minute + duration_minute

  while new_minute >= 60:
    new_minute -= 60
    new_hour += 1

  while new_hour >= 12:
    new_hour -= 12
    if am_pm == 'AM':
      am_pm = 'PM'
    elif am_pm == 'PM': 
      am_pm = 'AM'
      next_day += 1
  if new_hour == 0:
    new_hour = 12

  msg = r"{}:{:02d} {}".format(new_hour, new_minute, am_pm)

  if day != '':
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    new_day = week[(week.index(day.title()) + next_day) % 7]
    msg += ', ' + new_day

  if next_day == 1:
    msg += ' (next day)'
  elif next_day > 1:
    msg += ' ({} days later)'.format(next_day)
  
  return msg
    