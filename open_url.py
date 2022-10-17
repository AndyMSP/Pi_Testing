import subprocess

def open_url():
    subprocess.Popen(['/usr/bin/chromium-browser', '--new-window', '--start-fullscreen', 'https://web-01.tacobell.tech'])