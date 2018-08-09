import websockets
import asyncio
import datetime


async def ws_clock(websocket, path):
    while True:
        now = datetime.datetime.now()

        if len(str(now.hour)) < 2:
            hour = '0' + str(now.hour)
        else:
            hour = now.hour

        if len(str(now.minute)) < 2:
            minute = '0' + str(now.minute)
        else:
            minute = now.minute

        if len(str(now.second)) < 2:
            second = '0' + str(now.second)
        else:
            second = now.second

        time = '%s:%s:%s' % (hour, minute, second)
        await websocket.send(time)
        await asyncio.sleep(1)


start_server = websockets.serve(ws_clock, '127.0.0.1', 8003)

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()
