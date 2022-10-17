from flask import Flask
import subprocess
import logging
import time
import webbrowser
app = Flask(__name__)

@app.route("/open", strict_slashes=False)
def open():
    # subprocess.run(['pkill', 'chromium'])
    subprocess.Popen(['/usr/bin/chromium-browser', '--new-window', '--start-fullscreen', 'https://web-01.tacobell.tech'])
    return "200"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
