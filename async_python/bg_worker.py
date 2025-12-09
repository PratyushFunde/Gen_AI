import asyncio
import threading
import time

def backgroundWorker():
    while True:
        time.sleep(1)
        print(f"Log...")

async def fetchOrders():
    await time.sleep(3)
    print("Order fetched !")

threading.Thread(target=backgroundWorker,daemon=True).start()

asyncio.run(fetchOrders())