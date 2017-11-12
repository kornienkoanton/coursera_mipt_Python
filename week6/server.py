import asyncio

def run_server(host, port):
	loop = asyncio.get_event_loop()
	coro = loop.create_server(
		ClientServerProtocol,
		host, port
	)

	server = loop.run_until_complete(asyncio.wait_for(coro, 1))

	try:
		loop.run_forever()
	except KeyboardInterrupt:
		pass

	server.close()
	loop.run_until_complete(server.wait_closed())
	loop.close()

class ClientServerProtocol(asyncio.Protocol):
	data = []

	def __getattr__(self):
		return "error\nwrong property\n\n"

	def connection_made(self, transport):
		self.transport = transport

	def data_received(self, data):
		resp = self.process_data(data.decode())
		self.transport.write(resp.encode())

	def process_data(self, data):
		try:
			if data.endswith("\n"):
				if data.split()[0] == "put":
					request, key, value, timestamp = data.split()
					if f"{key} {value} {timestamp}\n" not in self.data:
						self.data.append(f"{key} {value} {timestamp}\n")
						print(self.data)
					return "ok\n\n"
				elif data.split()[0] == "get":
					respond = ""
					if data.split()[1] == "*":
						for metrix in self.data:
							respond += metrix
							print(respond)
						return "ok\n"+respond+"\n"
					else:
						for metrix in self.data:
							if data.split()[1] in metrix:
								respond += metrix
						return "ok\n"+respond+"\n"
				else:
					return "error\nwrong command\n\n"
			else:
				return "error\nwrong command\n\n"
		except:
			return "error\nwrong command\n\n"

if __name__=="__main__":
	run_server("127.0.0.1", 10001)