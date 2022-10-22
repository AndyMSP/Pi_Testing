#!/usr/bin/python3

import subprocess
import time
import os
import webbrowser

def turn_on():
    # subprocess.Popen(['/usr/bin/chromium-browser', '--new-window', '--start-fullscreen', 'https://web-01.tacobell.tech/pi/grandma'], shell=True)

    a = subprocess.Popen(['/usr/bin/chromium-browser', '--new-window', '--start-fullscreen', 'https://web-01.tacobell.tech/pi/grandma'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # webbrowser.open('https://web-01.tacobell.tech/pi/grandma')
    # os.execl('sudo', '-uandy', '/usr/bin/chromium-browser', '--new-window', '--start-fullscreen', 'https://web-01.tacobell.tech/pi/grandma')
    # time.sleep(10)
    # subprocess.run(['/home/andy/pi/tv_script.sh'])
    return 'f'



if __name__ == '__main__':
    turn_on()
