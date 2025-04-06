from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from deepseek_api import DeepseekAPI

app = Flask(__name__)

# Allow CORS for the frontend domain
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

# Initialize DeepseekAPI with your API key
deepseek_client = DeepseekAPI(api_key="sk-38b3cc0fab614a0cafd4ddca5fa12ee9")
# sk-38b3cc0fab614a0cafd4ddca5fa12ee9
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        api_response = deepseek_client.send_message(user_message)
        if 'reply' in api_response:
            return jsonify({'reply': api_response['reply']}), 200
        else:
            return jsonify({'error': api_response.get('error', 'Unknown error')}), 500
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)