
from time import sleep
import sys

def display_warning(cycles=6,sleep_time=1):
  for i in range(cycles):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(sleep_time)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(sleep_time)
    
def show_warning_message(message):
  print(message)
  
def vitals_ok(temperature, pulseRate, spo2):
  if temperature > 102 or temperature < 95:
    show_warning_message('Temperature critical!')
    display_warning()
    return False
  elif pulseRate < 60 or pulseRate > 100:
    show_warning_message('Pulse Rate is out of range!')
    display_warning()
    return False
  elif spo2 < 90:
    show_warning_message('Oxygen Saturation out of range!')
    display_warning()
    return False
  return True
