/**
 * Chat AI Frontend Application
 */

class ChatApp {
    constructor() {
        this.apiBaseUrl = 'http://localhost:5000/api';
        this.sessionId = this.generateSessionId();
        this.messagesContainer = document.getElementById('chatMessages');
        this.messageInput = document.getElementById('messageInput');
        this.sendBtn = document.getElementById('sendBtn');
        this.clearBtn = document.getElementById('clearBtn');
        this.modelSelect = document.getElementById('modelSelect');
        this.status = document.getElementById('status');

        this.init();
    }

    init() {
        this.sendBtn.addEventListener('click', () => this.sendMessage());
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.sendMessage();
        });
        this.clearBtn.addEventListener('click', () => this.clearChat());
        this.modelSelect.addEventListener('change', () => this.setModel());
    }

    generateSessionId() {
        return 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    }

    addMessage(content, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;

        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.textContent = content;

        messageDiv.appendChild(messageContent);
        this.messagesContainer.appendChild(messageDiv);

        // Scroll to bottom
        const chatContainer = document.querySelector('.chat-container');
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    async sendMessage() {
        const message = this.messageInput.value.trim();
        if (!message) return;

        // Add user message to chat
        this.addMessage(message, true);
        this.messageInput.value = '';
        this.setLoading(true);
        this.updateStatus('Sending...', 'normal');

        try {
            const response = await fetch(`${this.apiBaseUrl}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: message,
                    session_id: this.sessionId
                })
            });

            const data = await response.json();

            if (response.ok) {
                this.addMessage(data.response, false);
                this.updateStatus('Ready', 'success');
            } else {
                this.addMessage(`Error: ${data.error}`, false);
                this.updateStatus('Error occurred', 'error');
            }
        } catch (error) {
            this.addMessage(`Connection error: ${error.message}`, false);
            this.updateStatus('Connection error', 'error');
        }

        this.setLoading(false);
    }

    async clearChat() {
        try {
            await fetch(`${this.apiBaseUrl}/clear/${this.sessionId}`, {
                method: 'POST'
            });

            // Clear UI
            this.messagesContainer.innerHTML = '';
            this.addMessage('Chat cleared! How can I help you?', false);
            this.sessionId = this.generateSessionId();
            this.updateStatus('Chat cleared', 'success');
        } catch (error) {
            this.updateStatus('Error clearing chat', 'error');
        }
    }

    async setModel() {
        const model = this.modelSelect.value;

        try {
            const response = await fetch(`${this.apiBaseUrl}/model`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ model: model })
            });

            const data = await response.json();
            if (response.ok) {
                this.updateStatus(`Model: ${data.model}`, 'success');
            }
        } catch (error) {
            this.updateStatus('Error setting model', 'error');
        }
    }

    setLoading(loading) {
        this.sendBtn.disabled = loading;
        this.messageInput.disabled = loading;
        if (loading) {
            this.sendBtn.textContent = '...';
        } else {
            this.sendBtn.textContent = 'Send';
        }
    }

    updateStatus(text, type = 'normal') {
        this.status.textContent = text;
        this.status.className = `status ${type}`;
    }
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ChatApp();
});
