# asyncio, tcp сервер

import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print("received %r from %r" % (message, addr))
    resp = "ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n".encode()
    print("Send: %r" % resp)
    writer.write(resp)
    await writer.drain()

    print("Close the client socket")
    writer.close()
    
    return message

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, "127.0.0.1", 10001, loop=loop)
server = loop.run_until_complete(coro)
try:
    a = loop.run_forever()
    print(a)
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()