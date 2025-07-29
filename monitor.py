
from time import sleep
import sys

def warning(cycles=6,sleep_time=1):
  for i in range(cycles):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(sleep_time)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(sleep_time)
    
def show_warning(message):
  print(message)
  
def vitals_ok(temperature, pulseRate, spo2):
  if temperature > 102 or temperature < 95:
    show_warning('Temperature critical!')
    warning()
    return False
  elif pulseRate < 60 or pulseRate > 100:
    show_warning('Pulse Rate is out of range!')
    warning()
    return False
  elif spo2 < 90:
    show_warning('Oxygen Saturation out of range!')
    warning()
    return False
  return True
