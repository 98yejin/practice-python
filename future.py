import asyncio.futures
import concurrent.futures

MAX_WORKDERS = 10


def test(number):
    print(f"hello world! {number}")


with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKDERS) as executor:
    res = executor.map(test, [i for i in range(1, 10)])
