from prefect import task
import os
import logging

logging.basicConfig(level=logging.INFO)

@task
def fetch_account_cash():
    import httpx
    import asyncio
    import base64
    
    TRADING_212_URL = "https://live.trading212.com/"
    API_ENDPOINT = "api/v0/equity/account/cash"

    def credential(api: str, secret: str) -> str:
        credentials = f"{api}:{secret}"
        token = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        return token

    async def main():
        header = {"Authorization": f'Basic {credential(os.getenv("API_TOKEN"), os.getenv("SECRET_KEY"))}'}
        logging.info("Fetching account cash data from Trading 212 API")
        async with httpx.AsyncClient() as client:
            response = await client.get(TRADING_212_URL + API_ENDPOINT, headers=header)
            logging.info(f"Response received: {response.status_code}")
            if response.status_code == 200:
                logging.info("Account cash data fetched successfully")
                return response.json()
            else:
                logging.error(f"Error fetching account cash data: {response.status_code} - {response.text}")

    return asyncio.run(main())