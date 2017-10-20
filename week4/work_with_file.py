import os, tempfile

class File:
	"""File operator"""

	def __init__(self, file_path):
		self.file_path = file_path

	def __str__(self):
		return self.file_path

	def _read(self):
		with open(self.file_path, "r") as f:
			return f.read()

	def write(self, obj):
		with open (self.file_path, "w") as f:
			return f.write(obj)

	def __add__(self, obj):
		new_file = File(os.path.join(tempfile.gettempdir(), "temp.txt"))
		new_file.write(self._read() + "\n" + obj._read())
		return new_file

	def __getitem__(self, index):
		return self._read().split()[index]

if __name__ == "__main__":
	a = File("/home/anton/Documents/python notebook/training/text1.txt")
	b = File("/home/anton/Documents/python notebook/training/text2.txt")
	a.write("asd")
	b.write("zxc")
	c = a + b
	print(a,b,c)
	for row in c:
		print(row)