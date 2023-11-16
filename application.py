import openai
from flask import Flask, request, jsonify
import os
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

def setup_api_key():
    os.environ["OPENAI_API_KEY"] = 'YOUR_KEY_HERE'
    os.environ["OPENAI_MODEL"] = 'YOUR_MODEL_HERE'

@application.route('/hello', methods=['GET'])
def hello():
    return jsonify({"m": os.environ.get('OPENAI_MODEL'), "k":os.environ.get('OPENAI_API_KEY')}), 200

@application.route('/conversation', methods=['POST'])
def create_conversation():
    try:
        data = request.get_json()
        if 'messages' not in data:
            return jsonify({"error": "The 'messages' field is required."}), 400

        messages = data['messages']
        messages.insert(0, {"role":"system", "content": "YOUR_SYSTEM_ROLE"})

        model_name = os.environ.get('OPENAI_MODEL')

        response = openai.ChatCompletion.create(
            model=model_name,
            messages=messages
        )
        message_from_llm = response.choices[0].message['content']
        messages.append(message_from_llm)
        return jsonify({"response": response.choices[0].message['content']})

    except Exception as e:
        print("ERROR: " + str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    setup_api_key()
    application.run(debug=True)