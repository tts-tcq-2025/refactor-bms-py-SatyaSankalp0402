from warning import blinking_alert
from warning import print_warning_message

value_vitals = [
    ("temperature", 95, 102, "Temperature critical!", "Approaching Hypothermia", "Approaching Hyperthermia"),
    ("pulseRate", 60, 100, "Pulse Rate is out of range!", "Pulse dropping low", "Pulse Rising High"),
    ("spo2", 90, float("inf"), "Oxygen Saturation out of range!","Oxygen level dropping", None)
]

def vitals_ok(temperature, pulseRate, spo2):
    vitals = {
        "temperature": temperature,
        "pulseRate": pulseRate,
        "spo2": spo2
    }
    for vital_name, low, high, alert_message, warn_low_message, warn_high_message in value_vitals:
      value = vitals[vital_name]
      if high== float("inf"):
          tolerance=0
      else:
          tolerance=high*0.015

      #Early Warnings Detection
      if warn_low_message and (low<= value < low+tolerance):
          print_warning_message(f"Warning: {warn_low_message}")
      if warn_high_message and (high-tolerance < value <=high):
          print_warning_message(f"Warning: {warn_high_message}")

      # Critical Alerts    
      if (value < low) or (value > high):
          print_warning_message(alert_message)
          blinking_alert()
          return False
    return True
