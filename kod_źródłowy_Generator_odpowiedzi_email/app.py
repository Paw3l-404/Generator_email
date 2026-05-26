from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

app = Flask(__name__)
CORS(app, resources={r"/generate_reply": {"origins": "*"}})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_reply', methods=['POST'])
def generate_reply():
    data = request.get_json()

    email_text = data.get('emailText', '')
    decision = data.get('decision', '')
    tone = data.get('tone', '')

    if not email_text or decision not in ['tak', 'nie'] or tone not in ['formalny', 'nieformalny']:
        return jsonify({'error': 'Błędne dane wejściowe. Sprawdź wszystkie pola.'}), 400


    if decision == 'tak':
        prompt = f"Proszę odpowiedzieć na e-mail w sposób {'formalny' if tone == 'formalny' else 'nieformalny'} i zgodzić się na treść: {email_text}"
    else:  # decision == 'nie'
        prompt = f"Proszę odpowiedzieć na e-mail w sposób {'formalny' if tone == 'formalny' else 'nieformalny'} i odmówić: {email_text}"


    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return jsonify({'reply': response.text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
