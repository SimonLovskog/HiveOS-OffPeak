import aiohttp

apiUrl = "https://api2.hiveos.farm/api/v2"

async def getMinerStatus(farmID, workerID, APIKey):
    session = aiohttp.ClientSession(
        headers={"Authorization": "Bearer %s" % APIKey})

    data = await session.get("{}/farms/{}/workers/{}".format(apiUrl, farmID, workerID))
    data = await data.json()

    await session.close()

    return data["stats"]["online"]


async def turnOffOS(farmID, workerID, APIKey):
    session = aiohttp.ClientSession(
        headers={"Authorization": "Bearer %s" % APIKey})

    postBody = {
        "command": "shutdown",
        "data": {}
    }

    data = await session.post("{}/farms/{}/workers/{}/command".format(apiUrl, farmID, workerID), json=postBody)
    await session.close()
