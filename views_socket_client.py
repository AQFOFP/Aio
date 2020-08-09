import socketio

sio = socketio.Client()


@sio.on('connect')
def connect():
    print('connection established')


@sio.on('message')
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})


@sio.on('disconnect')
def disconnect():
    print('disconnected from server')


if __name__ == '__main__':
    sio.connect('http://127.0.0.1:9000')
    sio.emit('message', 'hai boy')
    sio.wait()


# import uuid
#
#
# def send_message(topic, data, room=None):
#     msg_id = str(uuid.uuid1())
#     _data = data.copy()
#     _data['msg_id'] = msg_id
#     if room:
#         sio.emit(topic, _data, room=room)
#     else:
#         sio.emit(topic, _data)
