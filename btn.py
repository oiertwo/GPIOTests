from gpiozero import Button
#from signal import 
from time import sleep


btn = Button(21)

btn.when_pressed = print("aaa")
btn.when_released = print("bbbb") 

sleep(10)

