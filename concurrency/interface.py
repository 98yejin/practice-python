import time
import asyncio


async def main():
    """
    This is the main function that prints a greeting, waits for 1 second, and then prints a farewell.
    """
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


def blocking():
    """
    This function introduces a blocking delay of 0.5 seconds and then prints a message.
    """
    time.sleep(0.5)
    print(f"{time.ctime()} Hello from a thread!")


loop = asyncio.get_event_loop()
task = loop.create_task(main())

loop.run_in_executor(None, blocking)
loop.run_until_complete(task)

pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)

loop.close()
