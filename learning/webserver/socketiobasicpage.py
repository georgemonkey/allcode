from aiohttp import web
import socketio

sio = socketio.AsyncServer(async_mode='aiohttp', async_handlers=True)
app=web.Application()
sio.attach(app)

async def index(request):
    return web.Response(text="Hello World", content_type="text/html")

app.router.add_get('/',index)

if __name__ == '__main__':
    web.run_app(app)