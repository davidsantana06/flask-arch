from flask_socketio import emit
from app.extensions import socket_io


@socket_io.on('message')
def handle_message(message):
    print('Received message:', message)
    emit('message', message)
