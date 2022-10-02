import asyncio
import websockets
from concurrent.futures import ThreadPoolExecutor
import re

# Add a asynchronous method to get input to allow the web socket to run in the background while we are waiting for input from the robot.
async def ainput(prompt: str = "") -> str:
    with ThreadPoolExecutor(1, "AsyncInput") as executor:
        return await asyncio.get_event_loop().run_in_executor(executor, input, prompt)

async def stream():
    async with websockets.connect("ws://localhost:3000/api/live/push/robot", extra_headers={'Authorization': 'Bearer eyJrIjoidkVyNW1kcU5lMWQxajl3MWtqUUVIV0NMdEc0clJ0dmIiLCJuIjoiUm9ib3QgR3JhZmFuYSBsaXZlIiwiaWQiOjF9'}) as websocket:
        i = 0

        while True:
            data = await ainput()

            try:
                data = data.split(":")
            except:
                continue
                
            if (len(data) == 2):
                name = data[0]
                value = data[1][1:]

                if re.search(r"[0-9-.]+", value) != None and value in re.search(r"[0-9-.]+", value).string:
                    await websocket.send(name + " " + name + "=" + value)
                else:
                    await websocket.send(name + " " + name + "=\"" + value + '"')

asyncio.run(stream())