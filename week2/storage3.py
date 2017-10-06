import os
import tempfile
import argparse
import json
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="input key")
parser.add_argument("--val", help="input value")
args = parser.parse_args()
key = args.key
value = args.val
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
data = None
if os.path.isfile(storage_path):
	with open(storage_path, "r+") as f:
		data = json.load(f)
elif value is None:
	print (None)
	exit()
else:
	with open(storage_path, "w+") as f:
		data = OrderedDict()
		data[key] = value
		json.dump(data, f)

#writing...
with open(storage_path, "w+") as f:
	if value is not None:
		data.setdefault(key, value)
		if data[key] != value:
			data[key] = data[key], value
	else:
		print (data.get(key, None))	
	json.dump(data, f)

