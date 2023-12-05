import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)

leitor = SimpleMFRC522()

texto = "Gustavo 12547739"

print("Aproxime a TAG do leitor...")
leitor.write(texto)

print("Concluido!")