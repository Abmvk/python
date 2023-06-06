from sense_hat import SenseHat

# Initialiseer de Sense HAT
sense = SenseHat()

# Vraag de gebruiker om invoer
message = input("Voer een tekst in: ")

# Stel de tekstkleur en achtergrondkleur in
tekst_kleur = (255, 255, 255)  # Wit
achtergrond_kleur = (0, 0, 0)  # Zwart

# Geef de tekst weer op het LED-scherm
sense.show_message(message, text_colour=tekst_kleur, back_colour=achtergrond_kleur)
