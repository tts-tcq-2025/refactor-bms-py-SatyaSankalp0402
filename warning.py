from time import sleep
import sys

def blinking_alert(cycles=6,sleep_time=1):
  for i in range(cycles):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(sleep_time)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(sleep_time)
    
def print_warning_message(message):
  print(message)
