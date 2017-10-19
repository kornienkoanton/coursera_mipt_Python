import os, tempfile

class File:
   """File operator"""

   def __init__(self, file_path):
      self.file_path = file_path

   def _read(self):
      with open(self.file_path, "r+") as f:
         return f.read()
   
   def __str__(self):
      return self.file_path

   def write(self, obj):
      with open (self.file_path, "w") as f:
         f.write(obj+"\n")
   
   def __add__(self, obj):
      with open(os.path.join(tempfile.gettempdir, "temp.txt"), "w+") as f:
         text = self._read()
         f.write(text)
      return text

   def __getitem__(self, index):
      return self._read()[index]

if __name__ == "__main__":
   a = File("/home/anton/Documents/python notebook/training/text1.txt")
   b = File("/home/anton/Documents/python notebook/training/text2.txt")
   a.write("asd")
   b.write("zxc")
   print (a)
   print(a + b)



