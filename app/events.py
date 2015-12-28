from flask import session
from flask.ext.socketio import emit, join_room, leave_room
from . import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):
    join_room('main')
    emit('status', {'msg': session.get('name') + ' зашел в наш уютный чатик'}, room='main')


@socketio.on('text', namespace='/chat')
def text(message):
    user_message = '<i>' + session.get('name') + '</i>: ' + message['msg']
    emit('message', {'msg': user_message}, room='main')


@socketio.on('left', namespace='/chat')
def left(message):
    leave_room('main')
    emit('status', {'msg': session.get('name') + ' куда-то свалил'}, room='main')
