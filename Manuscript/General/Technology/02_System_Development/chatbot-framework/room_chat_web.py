"""
PoetryAI Room Chat Web Interface
Simple Flask web app for the room chat system
"""

from flask import Flask, render_template, request, jsonify, session
import asyncio
import json
import uuid
from datetime import datetime
import sys
from pathlib import Path

# Add the chatbot-framework directory to Python path
sys.path.append(str(Path(__file__).parent))

from room_chat import (
    PoetryRoomChat,
    RoomType,
    create_room_1,
    create_room_2, 
    create_room_3,
    create_room_4
)

app = Flask(__name__)
app.secret_key = 'poetry_ai_research_2025'  # Change this in production

# Store active room instances
active_rooms = {}

# Room creation functions
ROOM_CREATORS = {
    'room_1': create_room_1,
    'room_2': create_room_2,
    'room_3': create_room_3, 
    'room_4': create_room_4
}

ROOM_INFO = {
    'room_1': {
        'name': 'Room 1: Structured + Aware',
        'description': 'Systematic responses with parameter transparency',
        'temperature': 0.3,
        'top_p': 0.4,
        'aware': True
    },
    'room_2': {
        'name': 'Room 2: Structured + Unaware', 
        'description': 'Systematic responses without parameter information',
        'temperature': 0.3,
        'top_p': 0.4,
        'aware': False
    },
    'room_3': {
        'name': 'Room 3: Exploratory + Aware',
        'description': 'Creative responses with parameter transparency', 
        'temperature': 0.8,
        'top_p': 0.9,
        'aware': True
    },
    'room_4': {
        'name': 'Room 4: Exploratory + Unaware',
        'description': 'Creative responses without parameter information',
        'temperature': 0.8,
        'top_p': 0.9,
        'aware': False
    }
}


@app.route('/')
def index():
    """Main page with room selection"""
    return render_template('index.html', rooms=ROOM_INFO)


@app.route('/room/<room_id>')
def room_chat(room_id):
    """Chat interface for specific room"""
    if room_id not in ROOM_INFO:
        return "Room not found", 404
    
    return render_template('chat.html', 
                         room_id=room_id,
                         room_info=ROOM_INFO[room_id])


@app.route('/api/start_session', methods=['POST'])
def start_session():
    """Start a new chat session"""
    data = request.json
    room_id = data.get('room_id')
    participant_id = data.get('participant_id', f'participant_{uuid.uuid4().hex[:8]}')
    
    if room_id not in ROOM_CREATORS:
        return jsonify({'error': 'Invalid room ID'}), 400
    
    try:
        # Create room instance
        room = ROOM_CREATORS[room_id]()
        
        # Start session
        welcome_message = room.start_session(participant_id)
        
        # Store room instance
        session_id = str(uuid.uuid4())
        active_rooms[session_id] = room
        
        # Store session ID in Flask session
        session['session_id'] = session_id
        session['room_id'] = room_id
        session['participant_id'] = participant_id
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'welcome_message': welcome_message,
            'room_info': ROOM_INFO[room_id]
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/send_message', methods=['POST'])
def send_message():
    """Send message and get response"""
    data = request.json
    user_message = data.get('message', '').strip()
    
    session_id = session.get('session_id')
    if not session_id or session_id not in active_rooms:
        return jsonify({'error': 'No active session'}), 400
    
    if not user_message:
        return jsonify({'error': 'Empty message'}), 400
    
    try:
        # Get room instance
        room = active_rooms[session_id]
        
        # Send message asynchronously
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        bot_response = loop.run_until_complete(room.send_message(user_message))
        loop.close()
        
        return jsonify({
            'success': True,
            'user_message': user_message,
            'bot_response': bot_response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/end_session', methods=['POST'])
def end_session():
    """End current session"""
    data = request.json
    session_notes = data.get('notes', '')
    
    session_id = session.get('session_id')
    if not session_id or session_id not in active_rooms:
        return jsonify({'error': 'No active session'}), 400
    
    try:
        # Get room instance
        room = active_rooms[session_id]
        
        # End session
        summary = room.end_session(session_notes)
        
        # Clean up
        del active_rooms[session_id]
        session.clear()
        
        return jsonify({
            'success': True,
            'summary': summary
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/get_history')
def get_history():
    """Get conversation history"""
    session_id = session.get('session_id')
    if not session_id or session_id not in active_rooms:
        return jsonify({'error': 'No active session'}), 400
    
    try:
        room = active_rooms[session_id]
        history = room.get_session_history()
        
        return jsonify({
            'success': True,
            'history': history
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/export_data')
def export_data():
    """Export session data"""
    session_id = session.get('session_id')
    if not session_id or session_id not in active_rooms:
        return jsonify({'error': 'No active session'}), 400
    
    try:
        room = active_rooms[session_id]
        export_file = room.export_room_data()
        
        return jsonify({
            'success': True,
            'export_file': export_file
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Create templates directory and files
def create_templates():
    """Create HTML templates"""
    templates_dir = Path(__file__).parent / 'templates'
    templates_dir.mkdir(exist_ok=True)
    
    # Index template
    index_html = '''<!DOCTYPE html>
<html>
<head>
    <title>PoetryAI Room Chat System</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; text-align: center; margin-bottom: 30px; }
        .room-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 20px; }
        .room-card { border: 1px solid #ddd; border-radius: 8px; padding: 20px; background: #fafafa; transition: transform 0.2s; }
        .room-card:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
        .room-title { font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 10px; }
        .room-desc { color: #666; margin-bottom: 15px; }
        .room-params { font-size: 12px; color: #888; margin-bottom: 15px; }
        .enter-btn { background: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; text-decoration: none; display: inline-block; }
        .enter-btn:hover { background: #2980b9; }
        .research-note { background: #fff3cd; border: 1px solid #ffeaa7; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎭 PoetryAI Research System</h1>
        
        <div class="research-note">
            <strong>Research Context:</strong> This system implements four experimental conditions for L2 poetry writing research. 
            Each room uses different AI parameters to study collaborative interaction patterns.
        </div>
        
        <div class="room-grid">
            {% for room_id, info in rooms.items() %}
            <div class="room-card">
                <div class="room-title">{{ info.name }}</div>
                <div class="room-desc">{{ info.description }}</div>
                <div class="room-params">
                    Temperature: {{ info.temperature }} | Top-p: {{ info.top_p }} | 
                    {% if info.aware %}Parameter Aware{% else %}Parameter Unaware{% endif %}
                </div>
                <a href="/room/{{ room_id }}" class="enter-btn">Enter Room</a>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>'''
    
    # Chat template  
    chat_html = '''<!DOCTYPE html>
<html>
<head>
    <title>{{ room_info.name }} - PoetryAI</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f5f5f5; display: flex; flex-direction: column; height: 100vh; }
        .header { background: #2c3e50; color: white; padding: 15px 20px; }
        .room-title { margin: 0; font-size: 20px; }
        .room-info { font-size: 14px; opacity: 0.8; margin-top: 5px; }
        .chat-container { flex: 1; display: flex; flex-direction: column; max-width: 800px; margin: 0 auto; width: 100%; padding: 20px; box-sizing: border-box; }
        .messages { flex: 1; overflow-y: auto; background: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .message { margin-bottom: 15px; }
        .user-msg { text-align: right; }
        .bot-msg { text-align: left; }
        .msg-content { display: inline-block; max-width: 80%; padding: 10px 15px; border-radius: 18px; word-wrap: break-word; }
        .user-msg .msg-content { background: #3498db; color: white; }
        .bot-msg .msg-content { background: #ecf0f1; color: #2c3e50; }
        .input-area { display: flex; gap: 10px; }
        .input-area input { flex: 1; padding: 12px; border: 1px solid #ddd; border-radius: 25px; outline: none; }
        .input-area button { background: #3498db; color: white; border: none; padding: 12px 20px; border-radius: 25px; cursor: pointer; }
        .input-area button:hover { background: #2980b9; }
        .input-area button:disabled { background: #bdc3c7; cursor: not-allowed; }
        .controls { text-align: center; margin-bottom: 20px; }
        .controls button, .controls input { margin: 0 5px; padding: 8px 15px; border-radius: 5px; }
        .start-btn { background: #27ae60; color: white; border: none; cursor: pointer; }
        .end-btn { background: #e74c3c; color: white; border: none; cursor: pointer; }
        .participant-input { border: 1px solid #ddd; }
        .status { text-align: center; padding: 10px; color: #666; font-style: italic; }
    </style>
</head>
<body>
    <div class="header">
        <div class="room-title">{{ room_info.name }}</div>
        <div class="room-info">{{ room_info.description }}</div>
    </div>
    
    <div class="chat-container">
        <div class="controls" id="controls">
            <input type="text" id="participantId" class="participant-input" placeholder="Enter participant ID" value="demo_participant">
            <button class="start-btn" onclick="startSession()">Start Session</button>
        </div>
        
        <div class="status" id="status">Enter participant ID and click "Start Session" to begin</div>
        
        <div class="messages" id="messages" style="display:none;"></div>
        
        <div class="input-area" id="inputArea" style="display:none;">
            <input type="text" id="messageInput" placeholder="Type your message..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()" id="sendBtn">Send</button>
            <button class="end-btn" onclick="endSession()">End Session</button>
        </div>
    </div>

    <script>
        let sessionActive = false;
        let sessionId = null;
        
        async function startSession() {
            const participantId = document.getElementById('participantId').value.trim();
            if (!participantId) {
                alert('Please enter a participant ID');
                return;
            }
            
            try {
                const response = await fetch('/api/start_session', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        room_id: '{{ room_id }}',
                        participant_id: participantId 
                    })
                });
                
                const data = await response.json();
                if (data.success) {
                    sessionId = data.session_id;
                    sessionActive = true;
                    
                    document.getElementById('controls').style.display = 'none';
                    document.getElementById('status').style.display = 'none';
                    document.getElementById('messages').style.display = 'block';
                    document.getElementById('inputArea').style.display = 'flex';
                    
                    addMessage('bot', data.welcome_message);
                    document.getElementById('messageInput').focus();
                } else {
                    alert('Error: ' + data.error);
                }
            } catch (error) {
                alert('Failed to start session: ' + error);
            }
        }
        
        async function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            if (!message || !sessionActive) return;
            
            addMessage('user', message);
            input.value = '';
            
            const sendBtn = document.getElementById('sendBtn');
            sendBtn.disabled = true;
            sendBtn.textContent = 'Thinking...';
            
            try {
                const response = await fetch('/api/send_message', {
                    method: 'POST', 
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: message })
                });
                
                const data = await response.json();
                if (data.success) {
                    addMessage('bot', data.bot_response);
                } else {
                    addMessage('bot', 'Error: ' + data.error);
                }
            } catch (error) {
                addMessage('bot', 'Connection error: ' + error);
            } finally {
                sendBtn.disabled = false;
                sendBtn.textContent = 'Send';
                input.focus();
            }
        }
        
        async function endSession() {
            if (!sessionActive) return;
            
            const notes = prompt('Session notes (optional):') || '';
            
            try {
                const response = await fetch('/api/end_session', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ notes: notes })
                });
                
                const data = await response.json();
                if (data.success) {
                    const summary = data.summary;
                    const summaryText = `Session ended!\\n\\nSummary:\\n- Interactions: ${summary.total_interactions}\\n- Duration: ${summary.duration_minutes} minutes\\n- Room: ${summary.room_type}`;
                    alert(summaryText);
                    
                    sessionActive = false;
                    location.href = '/';
                }
            } catch (error) {
                alert('Error ending session: ' + error);
            }
        }
        
        function addMessage(role, content) {
            const messages = document.getElementById('messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${role}-msg`;
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'msg-content';
            contentDiv.textContent = content;
            
            messageDiv.appendChild(contentDiv);
            messages.appendChild(messageDiv);
            messages.scrollTop = messages.scrollHeight;
        }
        
        function handleKeyPress(event) {
            if (event.key === 'Enter' && !event.shiftKey) {
                sendMessage();
            }
        }
    </script>
</body>
</html>'''
    
    # Write templates
    with open(templates_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    with open(templates_dir / 'chat.html', 'w', encoding='utf-8') as f:
        f.write(chat_html)


if __name__ == '__main__':
    # Create templates
    create_templates()
    
    print("🎭 PoetryAI Room Chat Web Interface")
    print("Setting up Flask application...")
    print("Visit http://localhost:5000 to access the chat system")
    
    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)