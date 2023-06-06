from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from math import atan2, degrees
import subprocess
import time

sense = SenseHat()

def display_temperature():
    # Lees de temperatuur uit en geef deze weer op het LED-scherm
    temperature = sense.get_temperature()
    temperature_str = f"{temperature:.1f}C"
    sense.show_message(temperature_str, text_colour=(0, 255, 0), back_colour=(0, 0, 0))

def get_cpu_temperature():
    # Gebruik de externe opdracht 'vcgencmd' om de CPU-temperatuur uit te lezen
    process = subprocess.Popen(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    temperature_str = output.decode().strip().split('=')[1]
    return float(temperature_str[:-2])

def display_cpu_temperature():
    # Lees de CPU-temperatuur uit en geef deze weer op het LED-scherm
    cpu_temperature = get_cpu_temperature()
    cpu_temperature_str = f"{cpu_temperature:.1f}C"
    sense.show_message(cpu_temperature_str, text_colour=(255, 0, 0), back_colour=(0, 0, 0))

def display_pressure():
    # Lees de luchtdruk uit en geef deze weer op het LED-scherm
    pressure = sense.get_pressure()
    pressure_str = f"{pressure:.1f}hPa"
    sense.show_message(pressure_str, text_colour=(0, 0, 255), back_colour=(0, 0, 0))

def display_compass_direction():
    # Weergeven van de hoek ten opzichte van het noorden op het LED-scherm
    north = sense.get_compass()
    angle = (360 - north) % 360
    angle_str = f"{angle:.0f}"
    sense.show_message(angle_str, text_colour=(255, 255, 255), back_colour=(0, 0, 0))

def handle_joystick(event):
    if event.action == ACTION_PRESSED or event.action == ACTION_HELD:
        if event.direction == "left":
            display_temperature()
        elif event.direction == "right":
            display_cpu_temperature()
        elif event.direction == "up":
            display_pressure()
        elif event.direction == "down":
            display_compass_direction()

try:
    sense.stick.direction_left = handle_joystick
    sense.stick.direction_right = handle_joystick
    sense.stick.direction_up = handle_joystick
    sense.stick.direction_down = handle_joystick

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    sense.clear()
