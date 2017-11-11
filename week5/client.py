import time, asyncio

class ClientError(Exception):
	pass

class Client():
	def __init__(self, host, port, timeout = None):
		self.host = host
		self.port = port
		self.timeout = timeout
		self.loop = asyncio.get_event_loop()

	async def tcp_echo_client(self, message):
		reader, writer = await asyncio.open_connection(self.host, self.port, loop=self.loop)
		writer.write(message.encode())
		data = await reader.read(100)
		writer.close()

		return data

	def put(self, key, value, timestamp = None):
		timestamp = timestamp or str(int(time.time()))
		message = "put {} {} {}\n".format(key, value, timestamp)
		respond = self.loop.run_until_complete(asyncio.wait_for(self.tcp_echo_client(message), self.timeout))
		if respond.decode() != "ok\n\n":
			raise ClientError
	
	def get(self, key):
		message = "get {}\n".format(key)
		respond = self.loop.run_until_complete(self.tcp_echo_client(message))
		final_data = {}
		#ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n
		if respond.decode().split()[0] == "ok":
			for data in respond.decode().split("\n")[1:]:
				if data:
					key, value, timestamp = data.split()
					if key not in final_data:
						final_data[key] = [(int(timestamp), float(value))]
					else:
						final_data[key].append((int(timestamp), float(value)))
						final_data[key].sort(key = lambda item: item[0])
		else:
			raise ClientError
		return final_data

	def close(self):
		self.loop.close()

if __name__ == "__main__":
	client = Client("127.0.0.1", 10001, timeout=5)
	client.put("test", 0.5, timestamp=1)
	client.put("test", 2.0, timestamp=2)
	client.put("test", 0.5, timestamp=3)
	client.put("load", 3, timestamp=4)
	client.put("load", 4, timestamp=5)
	print(client.get("*"))
	
	client.close()
