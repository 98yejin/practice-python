import asyncio
import time


async def main():
    """
    This is the main function that prints a greeting, waits for 1 second,
    and then prints a farewell message.
    """
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)
pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()

#  The  main  function prints a greeting, waits for 1 second, and then prints a farewell message. The  asyncio.get_event_loop()  function creates an event loop, and the  loop.create_task(main())  function creates a task that runs the  main  function. The  loop.run_until_complete(task)  function runs the task until it completes.
#  The  asyncio.all_tasks(loop=loop)  function gets all the tasks that are currently running in the event loop. The  for  loop iterates over the tasks and cancels them. The  asyncio.gather(*pending, return_exceptions=True)  function waits for all the tasks to complete. Finally, the  loop.close()  function closes the event loop.
#  Run the script with the following command:
#  python quickstart.py

#  The script prints the following output:
#  Mon Mar  7 12:00:00 2022 Hello!
