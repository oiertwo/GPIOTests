from gpiozero import LED
from time import sleep

uno = LED(17)
dos = LED(27)
tres = LED(4)

while True:
    uno.on()
    sleep(1)
    uno.off()
    dos.on()
    sleep(1)
    dos.off()
    tres.on()
    sleep(1)
    tres.off()
