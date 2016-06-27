from gpiozero import Button
from signal import pause
from time import sleep

btn = Button(21)

btn.when_pressed = lambda: print("aaa")
btn.when_released = lambda: print("bbbb") 

pause()
