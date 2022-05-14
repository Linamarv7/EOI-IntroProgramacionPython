#funcionaes asyncronicas q no se ejecuten en nuestro hilo
import asyncio #modulo

async def saludo(): #palabra reservada async antes de nuestra def
    print('Hola')
    await asyncio.sleep(4)
    print('...mundi')

asyncio.run(saludo())
print('Fin del programa')