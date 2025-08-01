from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit, send
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

users_typing = set()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    username = data['username']
    timestamp = datetime.now().strftime("%H:%M:%S")
    emit('message', {
        'type': 'system',
        'message': f'{username} joined the chat.',
        'timestamp': timestamp
    }, broadcast=True)

@socketio.on('send_message')
def handle_message(data):
    timestamp = datetime.now().strftime("%H:%M:%S")
    emit('message', {
        'username': data['username'],
        'message': data['message'],
        'timestamp': timestamp
    }, broadcast=True)

@socketio.on('typing')
def handle_typing(data):
    username = data['username']
    users_typing.add(username)
    emit('typing', list(users_typing), broadcast=True)

@socketio.on('stop_typing')
def handle_stop_typing(data):
    username = data['username']
    users_typing.discard(username)
    emit('typing', list(users_typing), broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
