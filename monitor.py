
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
    values_vitals= {
        'Temperature': (temperature, (95, 102), 'Temperature critical!'),
        'Pulse Rate': (pulseRate, (60, 100), 'Pulse Rate is out of range!'),
        'Oxygen Saturation': (spo2, (90, float('inf')), 'Oxygen Saturation out of range!')
        }
    for vital, (value, (low, high), message) in values_vitals.items():
      if (value < low) or (value > high):
          show_warning_message(message)
          display_warning()
          return False
    return True
