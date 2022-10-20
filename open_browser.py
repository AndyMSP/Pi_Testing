from flask import Flask
from turn_on import turn_on
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def open():
    turn_on()
    return "200"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
