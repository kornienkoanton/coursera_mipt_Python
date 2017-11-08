import time, asyncio

class Client():
	def __init__(self, host, port, timeout = None):
		self.host = host
		self.port = port
		self.timeout = timeout or 1

	async def tcp_echo_client(self, message, loop):
		reader, writer = await asyncio.open_connection(self.host, self.port, loop=loop)
		writer.write(message.encode())
		data = await reader.read(100)
		writer.close()

		return data

	def put(self, key, value, timestamp = None):
		timestamp = timestamp or str(int(time.time()))
		message = "put {} {} {}\n".format(key, value, timestamp)
		loop = asyncio.get_event_loop()
		respond = loop.run_until_complete(asyncio.wait_for(self.tcp_echo_client(message, loop), self.timeout))
		loop.close()
		if respond.decode() != "ok\n\n":
			raise ClientError
	
	def get(self, key):
		message = "get {}\n".format(key)
		loop = asyncio.get_event_loop()
		respond = loop.run_until_complete(self.tcp_echo_client(message, loop))
		loop.close()
		final_data = {}
		#ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n
		if respond.decode().split()[0] == "ok":
			for data in respond.decode().split("\n")[1:]:
				if data:
					key = data.split()[0]
					val1 = int(data.split()[1])
					val2 = float(data.split()[2])
					if key not in final_data:
						final_data[key] = [(val2, val1)]
					else:
						final_data[key].append((val2, val1))
						final_data[key].sort(key = lambda item: item[0])
		return final_data

class ClientError():
	pass