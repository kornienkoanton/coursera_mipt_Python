# asyncio, tcp клиент

import asyncio

async def tcp_echo_client(message, loop):
	reader, writer = await asyncio.open_connection("127.0.0.1", 10001, loop=loop)

	print("send: %r" % message)
	writer.write(message.encode())
	data = await reader.read(100)
	print('Received: %r' % data.decode())
	msg = 'Received: %r' % data.decode()

	print('Close the socket')
	writer.close()
	return msg

loop = asyncio.get_event_loop()
message = "hello World!"
msg = loop.run_until_complete(tcp_echo_client(message, loop))
print("final: {}".format(msg))
loop.close()