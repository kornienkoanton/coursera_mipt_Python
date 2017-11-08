import time, asyncio

class Client():
	def __init__(self, host, port, timeout = None):
		self.host = host
		self.port = port
		self.timeout = timeout
		self.data = None
		self.loop = asyncio.get_event_loop()

	async def tcp_echo_client(self, message):
		reader, writer = await asyncio.open_connection(self.host, self.port, loop=self.loop)

		print("send: %r" % message)
		writer.write(message.encode())
		data = await reader.read(100)
		self.data = data
   	print('Received: %r' % data.decode())
		if data.decode() != "ok\n\n":
			raise ClientError
   	print('Close the socket')
		writer.close()

	def put(self, key, value, timestamp = None):
		timestamp = timestamp or str(int(time.time()))
		try:
			message = "put {} {} {}\n".format(key, value, timestamp)
			data = self.loop.run_until_complete(self.tcp_echo_client(message))
			self.loop.close()
		except ClientError as err:
		self.data
		return {}
	
	def get(self, key):
		message = "get {}\n".format(key, value, timestamp)
		loop = asyncio.get_event_loop()
		loop.run_until_complete(self.tcp_echo_client(message, loop))
		loop.close()

		return {}
	
	server = loop.run_until_complete(coro)
	try:
		loop.run_until_complete()
	except KeyboardInterrupt:
		pass