from warning import blinking_alert
from warning import print_warning_message

value_vitals = [
    ("temperature", 95, 102, "Temperature critical!"),
    ("pulseRate", 60, 100, "Pulse Rate is out of range!"),
    ("spo2", 90, float("inf"), "Oxygen Saturation out of range!")
]

def vitals_ok(temperature, pulseRate, spo2):
    vitals = {
        "temperature": temperature,
        "pulseRate": pulseRate,
        "spo2": spo2
    }
    for vital_name, low, high, message in value_vitals:
      value = vitals[vital_name]
      if (value < low) or (value > high):
          print_warning_message(message)
          blinking_alert()
          return False
    return True
