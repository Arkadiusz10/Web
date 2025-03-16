import asyncio
import websockets

clients = set()

async def handler(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            # Wysyłanie wiadomości do wszystkich klientów
            await asyncio.gather(*[client.send(message) for client in clients if client != websocket])
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8000):
        await asyncio.Future()  # Utrzymuje serwer przy życiu

if __name__ == "__main__":
    asyncio.run(main())  # Poprawne uruchomienie pętli zdarzeń
