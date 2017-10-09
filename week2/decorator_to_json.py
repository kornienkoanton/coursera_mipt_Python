<<<<<<< HEAD
import json, functools

def to_json (func):
	@functools.wraps(func)
	def wrapped (*args,**kwargs):
		result = func(*args,**kwargs)
		return json.dumps(result)
	 
	return wrapped
=======
@to_json
def get_data():
	return {
	'data': 42
	}
  
get_data()  # вернёт '{"data": 42}'
>>>>>>> 3e26f3fca0c790e7d75aaea624325341360086cb
