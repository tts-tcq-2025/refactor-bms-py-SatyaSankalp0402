from warning import display_warning
from warning import show_warning_message
  
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
