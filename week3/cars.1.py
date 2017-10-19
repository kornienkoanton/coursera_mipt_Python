import csv, os

class CarBase:
	"""basic class"""

	def __init__(self, brand, photo_file_name, carrying):
		self.brand = brand
		self.photo_file_name = photo_file_name
		self.carrying = float(carrying)

	def get_photo_file_ext(self):
		return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
	"""class car"""

	car_type = "car"

	def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
		super().__init__(brand, photo_file_name, carrying)
		self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
	"""class truck"""
	
	car_type = "truck"	

	def __init__(self, brand, photo_file_name, carrying, body_whl):
		super().__init__(brand, photo_file_name, carrying)
		body_length, body_width, body_height = [0, 0, 0] if not body_whl else body_whl.split("x")		
		self.body_length = float(body_length)
		self.body_width = float(body_width)
		self.body_height = float(body_height) 
		
	def get_body_volume(self):
		return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
	"""class specmachine"""
	
	car_type = "spec_machine"

	def __init__(self, brand, photo_file_name, carrying, extra):
		super().__init__(brand, photo_file_name, carrying)
		self.extra = extra


def get_car_list(csv_filename):
	car_list = []
	with open(csv_filename) as csv_fd:
		reader = csv.reader(csv_fd, delimiter=';')
		next(reader)
		for row in reader:
			try:
				if row[0] == "car":
					car = Car(row[1], row[3], row[5], row[2])
				elif row[0] == "truck":
					car = Truck(row[1], row[3], row[5], row[4]) 
				elif row[0] == "spec_machine":
					car = SpecMachine(row[1], row[3], row[5], row[6])
				else:
					continue
				car_list.append(car)
			except (ValueError, IndexError):
				continue
	return car_list


if __name__ == "__main__":
	#csv_filename = sys.argv[1]
	csv_filename = "/media/anton/data/git/coursera_mipt_Python/week3/coursera_week3_cars.csv"
	#print (get_car_list(csv_filename))
	for obj in get_car_list(csv_filename):
		print (obj.get_photo_file_ext())