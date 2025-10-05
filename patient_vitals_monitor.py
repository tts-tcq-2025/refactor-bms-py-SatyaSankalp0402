from vitals_warning_system import blinking_alert
from vitals_warning_system import print_warning_message

vital_thresholds = {
    "temperature": (95, 102, "Temperature critical!", "Approaching Hypothermia", "Approaching Hyperthermia"),
    "pulseRate": (60, 100, "Pulse Rate is out of range!", "Pulse dropping low", "Pulse Rising High"),
    "spo2": (90, float("inf"), "Oxygen Saturation out of range!","Oxygen level dropping", None)
}
def calculate_tolerance(high):
    if high==float("inf"):
        return 0
    else:
        return high*0.015

def is_low_warning(value, low, tolerance):
    return low <= value < low + tolerance

def is_high_warning(value, high, tolerance):
    return high - tolerance < value <= high

def check_warnings(value, low, high, tolerance, warn_low_message, warn_high_message):
    warnings = {
        warn_low_message: (is_low_warning, low),
        warn_high_message: (is_high_warning, high)
    }

    for message, (check_func, limit) in warnings.items():
        if message and check_func(value, limit, tolerance):
            print_warning_message(f"Warning: {message}")
        
def check_critical(value, low, high, alert_message):
    if value < low or value > high:
        print_warning_message(alert_message)
        blinking_alert()
        return False
    return True


def check_vital_signs(temperature, pulseRate, spo2):
    current_vitals = {
        "temperature": temperature,
        "pulseRate": pulseRate,
        "spo2": spo2
    }
    for vital_name,value in current_vitals.items():
      low,high,alert_message,warn_low_message,warn_high_message = vital_thresholds[vital_name]
      tolerance=calculate_tolerance(high)
      check_warnings(value, low, high, tolerance, warn_low_message, warn_high_message)
      if not check_critical(value, low, high, alert_message):
            return False
    return True
