import os
import tempfile
import argparse
import json
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument("--key", type=str, help="input key")
parser.add_argument("--val", type=str, help="input value")
args = parser.parse_args()
key = args.key
value = args.val
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as f:
   data = OrderedDict()
   if value is None:
      print (data['key'])
   else:
      data["key"] = value  
   f.write(json.dumps(data))

