"""
Chat AI API - Python-based chat application using OpenAI API
"""

import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from chat_engine import ChatEngine

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize chat engine
chat_engine = ChatEngine(api_key=os.getenv("OPENAI_API_KEY"))

# Store chat sessions
chat_sessions = {}


@app.route("/api/chat", methods=["POST"])
def chat():
    """Handle chat messages."""
    data = request.json
    message = data.get("message")
    session_id = data.get("session_id", "default")

    if not message:
        return jsonify({"error": "Message is required"}), 400

    # Initialize session if not exists
    if session_id not in chat_sessions:
        chat_sessions[session_id] = []

    # Add user message to history
    chat_sessions[session_id].append({"role": "user", "content": message})

    # Get AI response
    response = chat_engine.get_response(chat_sessions[session_id])

    # Add AI response to history
    chat_sessions[session_id].append({"role": "assistant", "content": response})

    return jsonify({
        "response": response,
        "session_id": session_id,
        "message_count": len(chat_sessions[session_id])
    })


@app.route("/api/history/<session_id>", methods=["GET"])
def get_history(session_id):
    """Get chat history for a session."""
    if session_id not in chat_sessions:
        return jsonify({"error": "Session not found"}), 404

    return jsonify({
        "session_id": session_id,
        "history": chat_sessions[session_id]
    })


@app.route("/api/clear/<session_id>", methods=["POST"])
def clear_history(session_id):
    """Clear chat history for a session."""
    if session_id in chat_sessions:
        chat_sessions[session_id] = []
    return jsonify({"message": "History cleared", "session_id": session_id})


@app.route("/api/models", methods=["GET"])
def get_models():
    """Get available models."""
    return jsonify({
        "models": chat_engine.get_available_models()
    })


@app.route("/api/model", methods=["POST"])
def set_model():
    """Set the model to use."""
    data = request.json
    model = data.get("model")

    if not model:
        return jsonify({"error": "Model is required"}), 400

    chat_engine.set_model(model)
    return jsonify({"message": f"Model set to {model}", "model": model})


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "message": "Chat AI API is running"})


if __name__ == "__main__":
    print("=" * 50)
    print("  Chat AI API Server")
    print("=" * 50)
    print("Starting server on http://localhost:5000")
    print("Endpoints:")
    print("  POST /api/chat - Send a message")
    print("  GET  /api/history/<session_id> - Get chat history")
    print("  POST /api/clear/<session_id> - Clear chat history")
    print("  GET  /api/models - Get available models")
    print("  POST /api/model - Set model")
    print("=" * 50)
    app.run(debug=True, port=5000)
