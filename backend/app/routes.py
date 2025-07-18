# app/routes.py
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.ml.predict import predict
from app.hibp.hibp import check_pwned
from app.llm.llm_helper import generate_password_advice

bp = Blueprint('api', __name__)

@bp.route('/predict_password', methods=['POST', 'OPTIONS'])  # dozvoli OPTIONS
@cross_origin()  # automatski doda CORS headere i odgovori na preflight
def predict_password():
    if request.method == 'OPTIONS':
        # Browser preflight -> samo odgovori OK
        return jsonify({'status': 'ok'}), 200

    data = request.get_json()
    password = data.get('password', '')

    # ML strength prediction
    strength = predict(password)

    # HIBP breach check
    hibp_result = check_pwned(password)

    # LLM advice
    llm_advice = generate_password_advice(password, strength)

    return jsonify({
        'strength': strength,
        'hibp': hibp_result,
        'llm_advice': llm_advice
    })
