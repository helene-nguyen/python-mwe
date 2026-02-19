"""
Asyncio example (for asynchronous I/O)
"""
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # simulate async I/O
    print("World")

async def main():
    await asyncio.gather(say_hello(), say_hello())

asyncio.run(main())