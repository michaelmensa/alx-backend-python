# Python - Async

## 1. Async and Await Syntax

In Python, asynchronous programming is facilitated by the use of the `async` and `await` keywords. These keywords allow you to define asynchronous functions and pause their execution until the awaited operation completes. Here's an example:

```python
async def example_async_function():
    print("Start of async function")
    await asyncio.sleep(1)
    print("End of async function")

# To run the async function, you need an event loop
import asyncio
asyncio.run(example_async_function())
```

In the example above, `asyncio.sleep(1)` is an asynchronous operation, and `await` is used to pause the execution of the function until the sleep is completed.

## 2. Executing an Async Program with asyncio

To execute an async program, you need to create an event loop using `asyncio` and run the async functions within it. The `asyncio.run()` function is commonly used for this purpose:

```python
import asyncio

async def main():
    await example_async_function()

asyncio.run(main())
```

In this example, the `main()` function is an entry point for the async program.

## 3. Running Concurrent Coroutines

Asyncio allows you to run multiple coroutines concurrently using `asyncio.gather()` or `asyncio.create_task()`:

```python
async def coroutine1():
    # ...

async def coroutine2():
    # ...

# Using asyncio.gather()
await asyncio.gather(coroutine1(), coroutine2())

# Using asyncio.create_task()
task1 = asyncio.create_task(coroutine1())
task2 = asyncio.create_task(coroutine2())
await task1
await task2
```

## 4. Creating Asyncio Tasks

Tasks in asyncio represent units of work to be done concurrently. You can create tasks using `asyncio.create_task()`:

```python
async def example_task():
    # ...

task = asyncio.create_task(example_task())
await task
```

## 5. Using the Random Module

The `random` module in Python provides functions for generating random numbers. When used in async programs, you may need to be cautious about concurrency. Here's an example:

```python
import random
import asyncio

async def random_operation():
    await asyncio.sleep(1)
    result = random.randint(1, 100)
    print(f"Random result: {result}")

# Running multiple random operations concurrently
await asyncio.gather(random_operation(), random_operation())
```

In this example, `random.randint(1, 100)` generates a random integer between 1 and 100 asynchronously.

These concepts provide a foundation for understanding asynchronous programming in Python using the asyncio module.
