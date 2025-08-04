
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
    value_vitals = [
        (temperature, 95, 102, 'Temperature critical!'),
        (pulseRate, 60, 100, 'Pulse Rate is out of range!'),
        (spo2, 90, float('inf'), 'Oxygen Saturation out of range!')
    ]
    for value, low, high, message in value_vitals:
      if (value < low) or (value > high):
          show_warning_message(message)
          display_warning()
          return False
    return True
