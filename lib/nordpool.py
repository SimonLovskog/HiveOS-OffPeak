import aiohttp

async def getPrice(date):
    session = aiohttp.ClientSession()
    correctedDate = "{}-{}-{}".format(str(date.year), str(date.month), str(date.day))

    data = await session.get("https://www.vattenfall.se/api/price/spot/pricearea/%s/%s/SN4" % (correctedDate, correctedDate))
    await session.close()

    return await data.json()

async def getCurrentPrice(data, date):
    return data[date.hour]["Value"]