# main.py
from flask import Flask
from flask_cors import CORS
from app.routes import bp
from dotenv import load_dotenv

app = Flask(__name__)

# Omogućava CORS svuda (React -> Flask)
CORS(app)

load_dotenv()

# Registruje blueprint sa prefixom /api (bitno za React poziv)
app.register_blueprint(bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
