import time
import os
import aiohttp
import asyncio
from datetime import datetime

from lib.nordpool import *
from lib.kasa import *
from lib.hiveos import *

sleepTime = 60

async def main(farmID, workerID, APIKEY, powerCostThreshold):
    while True:
        print("Updating data.")
        now = datetime.now()
        nordPoolPrice = await getPrice(now.date())
        minerRunning = await getMinerStatus(farmID, workerID, APIKEY)
        await update()

        price = await getCurrentPrice(nordPoolPrice, now)
        print("Current price is %s" % str(price))

        if price <= powerCostThreshold:
            print("Starting Plug.")
            await turnOn()
            await asyncio.sleep(sleepTime)
            continue

        if minerRunning: 
            print("Stopping OS.")
            await turnOffOS(farmID, workerID, APIKey)
        
        if await isOn() and not minerRunning:
            print("Stopping Plug.")
            await turnOff()

        await asyncio.sleep(sleepTime)

if __name__ == '__main__':
    farmID = os.getenv("FARMID")
    workerID = os.getenv("WORKERSID")
    APIKey = os.getenv("APIKEY")
    powerCostThreshold = os.getenv("THRESHOLD")

    asyncio.run(main(farmID, workerID, APIKey, int(powerCostThreshold)))
