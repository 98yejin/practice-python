import asyncio


async def async_fizzbuzz(n):
    results = {}

    async def handle_number(i):
        nonlocal results
        if i % 3 == 0 and i % 5 == 0:
            results[i] = "FizzBuzz"
        elif i % 3 == 0:
            results[i] = "Fizz"
        elif i % 5 == 0:
            results[i] = "Buzz"
        else:
            results[i] = str(i)

    tasks = [handle_number(i) for i in range(1, n + 1)]
    await asyncio.gather(*tasks)
    for i in sorted(results):
        print(results[i])


asyncio.run(async_fizzbuzz(10))
