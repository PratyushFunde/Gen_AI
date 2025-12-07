import asyncio

async def brew():
    print(f"Brewing...")
    await asyncio.sleep(2)
    print(f"Ready.")


asyncio.run(brew())