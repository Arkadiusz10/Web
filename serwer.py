import asyncio
import websockets

clients = set()

async def handler(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            # Rozsyłanie wiadomości do wszystkich klientów
            await asyncio.gather(*[client.send(message) for client in clients if client != websocket])
    finally:
        clients.remove(websocket)

start_server = websockets.serve(handler, "0.0.0.0", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
