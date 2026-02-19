import time

# Before optimization of loop
def square_numbers_loop(numbers):
    result = []
    for number in numbers:
        result.append(number)  # Simulate a time-consuming operation
    return result

test_numbers = list(range(1000000))

start_time = time.time()
squared_numbers = square_numbers_loop(test_numbers)
loop_time = time.time() - start_time

print(f"Loop completed in {loop_time:.4f} seconds")
# loop_time:.4f how many numbers after the decimal point

def square_numbers_comprehension(numbers):
    return [number ** 2 for number in numbers]  # Simulate a time-consuming operation

start_time = time.time()
squared_numbers_comp = square_numbers_comprehension(test_numbers)
comprehension_time = time.time() - start_time
print(f"Comprehension completed in {comprehension_time:.4f} seconds")
# Comparing the two methods
print(f"Improvement: {loop_time / comprehension_time:.2f}x faster with comprehension")

# coroutine
# Coroutines are a more generalized form of subroutines. Subroutines are entered at one point and exited at another point. Coroutines can be entered, exited, and resumed at many different points. They can be implemented with the async def statement. See also PEP 492.

# coroutine function
# A function which returns a coroutine object. A coroutine function may be defined with the async def statement, and may contain await, async for, and async with keywords. These were introduced by PEP 492.

import asyncio

async def main():
    """
    async def defines a coroutine function.
    await pauses the execution of the coroutine until the awaited task (asyncio.sleep(1), simulating an I/O operation) completes.
    asyncio.run() executes the coroutine and runs the event loop

    Note:
    - Functions defined with async def syntax are always coroutine functions, even if they do not contain await or async keywords.

    Reference:
        https://docs.python.org/3/reference/compound_stmts.html#async-def:~:text=Functions%20defined%20with%20async%20def%20syntax%20are%20always%20coroutine%20functions%2C%20even%20if%20they%20do%20not%20contain%20await%20or%20async%20keywords.

    Example:
        async def func(param1, param2):
           do_stuff()
           await some_coroutine()
    """
    print('hello')
    await asyncio.sleep(1)
    return 'world'

world = asyncio.run(main())
print('type of world', type(world))


async def task(i):
    await asyncio.sleep(1)
    return i

async def main_async():
    # Option 1: Use gather directly with coroutine objects.
    results = await asyncio.gather(task(1), task(2))  # Both run concurrently
    print(results)  # [1, 2]

    # Option 2: Use create_task for "fire-and-forget" or for finer control.
    t1 = asyncio.create_task(task(3))
    t2 = asyncio.create_task(task(4))
    res1 = await t1
    res2 = await t2
    print([res1, res2])

    # Option 3: Mix both—create tasks, then gather.
    t3 = asyncio.create_task(task(5))
    t4 = asyncio.create_task(task(6))
    results = await asyncio.gather(t3, t4)
    print(results)

asyncio.run(main_async())


