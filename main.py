from aiohttp import web
from routes import setup_routes
from settings import config
from views_socket import sio

app = web.Application()
setup_routes(app)
sio.attach(app)

app['config'] = config
web.run_app(app, port=9000)