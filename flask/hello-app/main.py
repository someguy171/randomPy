from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    
    return """<button type="Button">Hello</button>"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)