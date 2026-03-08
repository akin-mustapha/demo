import sys
import asyncio
from bleak import BleakScanner, BleakClient


class BLE_Client:
    def __init__(self, address):
        self.address = address
        self.client = None

    async def connect(self):
        self.client = BleakClient(self.address)
        await self.client.connect()
        print(f"Connected to {self.address}")

    async def disconnect(self):
        await self.client.disconnect()
        print(f"Disconnected from {self.address}")

    async def read_characteristic(self, characteristic_uuid):
        if self.client.is_connected:
            data = await self.client.read_gatt_char(characteristic_uuid)
            print(f"Data from {characteristic_uuid}: {data}")
        else:
            print("Client is not connected.")

    def get_services(self):
        if self.client.is_connected:
            services = self.client.services
            print("Services:")
            print(services.get_descriptor(14))
            for service in services:
                print(f"\nService: {service}")
                for characteristic in service.characteristics:
                    print(f"Characteristic: {characteristic.uuid}, Properties: {characteristic.properties}")
        else:
            print("Client is not connected.")


if __name__ == "__main__":
    
    # Replace with the address of your BLE device
    device_address = sys.argv[1]
    client = BLE_Client(device_address)

    async def main():
        await client.connect()
        client.get_services()
        await client.disconnect()

    asyncio.run(main())