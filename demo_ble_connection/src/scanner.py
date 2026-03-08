import asyncio
from bleak import BleakScanner


async def run_scanner():
    print("Starting scanner...")
    devices = await BleakScanner.discover()
    print("Devices found:")
    for device in devices:
        print(f"Device: {device.name}, Address: {device.address}")
    print("Scanner finished.")
    print("Waiting for 5 seconds...")
    await asyncio.sleep(5)
    print("Scanner finished.")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_scanner())
    loop.close()