import asyncio

# Define an asynchronous function using async def
async def fetch_data():
    print("Fetching data...")
    # Simulate an I/O-bound operation with asyncio.sleep
    await asyncio.sleep(3)
    print("Data fetched!")
    return "Some data"

# Define anther asynchronous function that uses await
async def main():
    print("Start fetching data")
    # Await the fetch_data coroutine, pausing main() until fetch_data() completes
    data = await fetch_data()
    print("Received data: {}".format(data))

# Run the main function using asyncio.run to execute the event loop
asyncio.run(main())
