import os
from kasa import SmartPlug

p = SmartPlug(os.getenv("PLUGIP"))

async def update():
    await p.update()

async def isOn():
    return p.is_on

async def turnOff(): 
    await p.turn_off()

async def turnOn():
    await p.turn_on()
