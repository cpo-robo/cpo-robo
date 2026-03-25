from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
import json

app = Flask(__name__)
CORS(app)

# Initialize OpenAI client
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("⚠️  WARNING: OPENAI_API_KEY environment variable not set!")
    print("Please set your OpenAI API key before running the server.")
    print("Visit https://platform.openai.com/account/api-keys to get your API key.")

client = OpenAI(api_key=api_key)

# Load the permit guide JSON for context
PERMIT_GUIDE_PATH = os.path.join(os.path.dirname(__file__), 'Syracuse_Permit_Guide_RAG.json')
permit_guide_context = None

try:
    with open(PERMIT_GUIDE_PATH, 'r') as f:
        permit_guide_data = json.load(f)
        # Create context string from chunks
        permit_guide_context = "## Syracuse Residential Permit Guide\n\n"
        for chunk in permit_guide_data.get('chunks', []):
            permit_guide_context += f"### {chunk['title']}\n{chunk['content']}\n\n"
except FileNotFoundError:
    print(f"⚠️  Warning: {PERMIT_GUIDE_PATH} not found. Using ChatGPT knowledge only.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests and return ChatGPT's response"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'error': 'Empty message'}), 400

        if not api_key:
            return jsonify({'error': 'API key not configured. Please set OPENAI_API_KEY environment variable.'}), 500

        # Build the system prompt with permit guide context
        system_prompt = """You are CPO Robo, a Centralized Permitting Bot for the City of Syracuse.
You help residents understand the permit process for new residential builds and modular homes.

You have access to the City of Syracuse Residential Permit Guide. Use this information to answer questions accurately.
Be helpful, clear, and professional. If you don't know something, say so honestly.
Provide specific contact information and links when relevant."""

        if permit_guide_context:
            system_prompt += f"\n\n## Reference Materials:\n{permit_guide_context}"

        # Call OpenAI API with gpt-4o-mini (cheapest and fast)
        message = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=1024,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        # Extract response text
        response_text = message.choices[0].message.content

        return jsonify({
            'response': response_text,
            'usage': {
                'input_tokens': message.usage.prompt_tokens,
                'output_tokens': message.usage.completion_tokens
            }
        })

    except Exception as e:
        print(f"OpenAI API Error: {str(e)}")
        return jsonify({'error': f'OpenAI API error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'online',
        'api_configured': bool(api_key),
        'permit_guide_loaded': permit_guide_context is not None
    })

if __name__ == '__main__':
    if not api_key:
        print("\n" + "="*60)
        print("ERROR: OPENAI_API_KEY not set!")
        print("="*60)
        print("\nTo set your API key, run:")
        print('  set OPENAI_API_KEY=your-key-here')
        print("\nOr edit SET_API_KEY.bat and add your key there.")
        print("\nGet your API key from: https://platform.openai.com/account/api-keys")
        print("="*60 + "\n")
    else:
        print("\n✓ OpenAI API key detected")
        print("✓ Using gpt-4o-mini (cheapest & fastest)")
        print("✓ Starting CPO Robo Permit Bot...")

    app.run(host='127.0.0.1', port=5000, debug=False)
