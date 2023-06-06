from sense_hat import SenseHat

sense = SenseHat()

def set_display(color):
    # Vorm een gekleurd vlak op het LED-scherm
    sense.clear(color)

def display_temperature():
    # Lees de temperatuur uit en geef deze weer op het LED-scherm
    temperature = sense.get_temperature()
    temperature_str = f"{temperature:.1f}C"
    sense.set_rotation(90)  # Rotatie van 90 graden
    sense.show_message(temperature_str, text_colour=(0, 255, 0), back_colour=(0, 0, 0))
    sense.set_rotation(0)  # Herstel de rotatie naar de standaardwaarde

def display_pressure():
    # Lees de luchtdruk uit en geef deze weer op het LED-scherm
    pressure = sense.get_pressure()
    pressure_str = f"{pressure:.1f}hPa"
    sense.set_rotation(90)  # Rotatie van 90 graden
    sense.show_message(pressure_str, text_colour=(255, 0, 0), back_colour=(0, 0, 0))
    sense.set_rotation(0)  # Herstel de rotatie naar de standaardwaarde

try:
    while True:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    set_display((0, 0, 255))  # Blauw vlak
                elif event.direction == "down":
                    set_display((255, 255, 0))  # Geel vlak
                elif event.direction == "left":
                    display_temperature()
                elif event.direction == "right":
                    display_pressure()

except KeyboardInterrupt:
    sense.clear()  # Wis het LED-scherm bij het stoppen van het programma
