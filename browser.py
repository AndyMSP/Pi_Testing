#!/usr/bin/python3
"""opens a browser"""

def open_chromium():
    """open chromium to webpage"""
    import subprocess
    subprocess.Popen(['/usr/bin/chromium-browser', '--new-window', '--start-fullscreen', 'https://web-01.tacobell.tech/pi/grandma'])


if __name__ == '__main__':
    open_chromium()