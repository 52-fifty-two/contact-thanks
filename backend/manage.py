from flask import Flask
from flask_cors import CORS

from api.api import api_bp

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://127.0.0.1", "https://contact-thanks.netlity.app"]}})

@app.route("/")
def hello_world():
    return {"message": "Hello, World!"}

app.register_blueprint(api_bp, url_prefix="/api")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)