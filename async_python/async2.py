import asyncio
import time

async def brew(name):
    print(f"Brewing : {name}")
    await asyncio.sleep(3)
    print(f"Done brewing : {name}")

async def main():
    start = time.time()
    await asyncio.gather(
        brew("Masala"),
        brew("Ginger"),
        brew("Green"),
    )
    end=time.time()

    print(f"Total time taken is : {end-start:.2f}")

asyncio.run(main())