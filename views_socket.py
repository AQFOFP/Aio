import socketio
from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

# mgr = socketio.AsyncRedisManager('redis://localhost:6379/0')
# sio = socketio.AsyncServer(client_manager=mgr)


@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)


@sio.on('message')
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit('reply', room=sid)


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    web.run_app(app, port=9000)

    '''
    需求：
    有一个进程用于订阅redis指定的消息，当有订阅消息发过来的时候，
    通过sio.emit(topic, _data)发送消息给客户端
    客户端接收到消息时，处理内容
    '''