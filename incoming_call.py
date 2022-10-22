from flask import Flask
from turn_on import turn_on
import subprocess
import time
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def open():
    print('calling sub next')
    subprocess.run(['/usr/bin/chromium-browser', 'google.com'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print('finished calling sub, starting sleep')
    time.sleep(10)
    print('finished sleep, returning value')
    return 'done'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
