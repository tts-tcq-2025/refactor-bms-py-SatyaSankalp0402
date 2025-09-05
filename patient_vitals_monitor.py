from vitals_warning_system import blinking_alert
from vitals_warning_system import print_warning_message

vital_thresholds = {
    "temperature": (95, 102, "Temperature critical!", "Approaching Hypothermia", "Approaching Hyperthermia"),
    "pulseRate": (60, 100, "Pulse Rate is out of range!", "Pulse dropping low", "Pulse Rising High"),
    "spo2": (90, float("inf"), "Oxygen Saturation out of range!","Oxygen level dropping", None)
}

def check_vital_signs(temperature, pulseRate, spo2):
    current_vitals = {
        "temperature": temperature,
        "pulseRate": pulseRate,
        "spo2": spo2
    }
    for vital_name,value in current_vitals.items():
      low,high,alert_message,warn_low_message,warn_high_message = vital_thresholds[vital]
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
