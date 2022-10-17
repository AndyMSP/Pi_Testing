from flask import Flask
import os
import time
app = Flask(__name__)

@app.route("/open", strict_slashes=False)
def open():
    # subprocess.run(['pkill', 'chrome'])
    os.system('chromium-browser --new-window --start-fullscreen https://web-01.tacobell.tech')
    return "200"

if __name__ == "__main__":
    app.run(host='0.0.0.0')