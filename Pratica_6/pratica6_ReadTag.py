import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

#Inicializando com os pinos baixos
GPIO.output(2, GPIO.LOW)
GPIO.output(3, GPIO.LOW)

leitor = SimpleMFRC522()

while True:

    id, texto = leitor.read()

    if((texto.strip() == "Gustavo 12547739") and (id == 427594131155)):
        print("Tag reconhecida, Acesso liberado!")
        #LED Verde acende
        GPIO.output(2, GPIO.HIGH)
    else:
        print("Acesso Negado!")
        #LED Vermelho acende
        GPIO.output(3, GPIO.HIGH)

    sleep(3)

    #Reseta os pinos para LOW novamente
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
