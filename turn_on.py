#!/usr/bin/python3

import subprocess
import time

def turn_on():
    # subprocess.Popen(['chromium-browser', '--new-window', '--start-fullscreen', 'https://web-01.tacobell.tech/pi/grandma'])
    subprocess.run(['/home/andy/Pi_Testing/tv_script'])
    subprocess.Popen(['chromium-browser', '--new-window', '--start-fullscreen', 'https://web-01.tacobell.tech/pi/grandma'])
    return "hello"



if __name__ == '__main__':
    turn_on()
