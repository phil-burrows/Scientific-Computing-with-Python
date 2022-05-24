def add_time(start, duration, dayOfWeek=""):

  ## Deconstruct start time
  time = start.replace(':',' ')
  time = time.split(' ')
  if time[2] == 'PM':
    time[0] = int(time[0]) + 12
    
  ## Deconstruct duration
  duration = duration.split(':')
    
  ## Fill new time placeholders
  hours = int(time[0]) + int(duration[0])
  minutes = int(time[1]) + int(duration[1])

  ## Fix minutes
  if minutes >= 60:
    addHours = minutes // 60
    hours += addHours
    minutes -= addHours * 60
    minutes = str(minutes).rjust(2,'0')
  else:
    minutes = str(minutes).rjust(2,'0')

  ## Find assign AM or PM
  AMPM = (hours // 12) % 2
  if AMPM == 0:
    AMPM = 'AM'
  else:
    AMPM = 'PM'

  ## Calculate days length
  days = hours // 24

  ## Fix hours
  hours = hours % 12
  if hours == 0:
    hours += 12
  
  ## Fix dayOfWeek
  week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

  if dayOfWeek:
    dayName = dayOfWeek.capitalize()
    dayPosition = week.index(f'{dayName}')
    dayPosition += days
    dayPosition %= 7
    newDayName = week[dayPosition]
    
### Build out returns
  
  ## Same day
  if days == 0:
    if dayOfWeek:
      new_time = f"{hours}:{minutes} {AMPM}, {newDayName}"
    else:
      new_time = f"{hours}:{minutes} {AMPM}"
  
  ## Next day
  if days == 1:
    if dayOfWeek:
      new_time = f"{hours}:{minutes} {AMPM}, {newDayName} (next day)"
    else:
      new_time = f"{hours}:{minutes} {AMPM} (next day)"

  ## Days later
  if days > 1:
    if dayOfWeek:
      new_time = f"{hours}:{minutes} {AMPM}, {newDayName} ({days} days later)"
    else:
      new_time = f"{hours}:{minutes} {AMPM} ({days} days later)"
  
  return new_time