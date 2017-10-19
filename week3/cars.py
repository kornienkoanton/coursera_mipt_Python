import csv, os

class CarBase:
	def __init__(self, car_type, brand, photo_file_name, carrying):
		self.brand = brand
		self.photo_file_name = photo_file_name
		self.carrying = float(carrying)
		self.car_type = car_type

	def get_photo_file_ext(self):
		return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
	def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
		super().__init__(car_type, brand, photo_file_name, carrying)
		self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
	def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
		super().__init__(car_type, brand, photo_file_name, carrying)
		body_length, body_width, body_height = [0, 0, 0] if not body_whl else body_whl.split("x")		
		#if body_whl:
		#	body_length, body_width, body_height = body_whl.split("x")
		#else:
		#	body_length, body_width, body_height = 0, 0, 0
		self.body_length = float(body_length)
		self.body_width = float(body_width)
		self.body_height = float(body_height) 
		
	def get_body_volume(self):
		return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
	def __init__(self, car_type, brand, photo_file_name, carrying, extra):
		super().__init__(car_type, brand, photo_file_name, carrying)
		self.extra = extra


def get_car_list(csv_filename):
	car_list = []
	with open(csv_filename) as csv_fd:
		reader = csv.reader(csv_fd, delimiter=';')
		next(reader)
		for row in reader:
			try:
				if row[2] and row[0] == "car" and row[1] and row[3] and row[5]:
					car = Car(row[0], row[1], row[3], row[5], row[2])
				elif row[0] == "truck" and row[1] and row[3] and row[5]:
					car = Truck(row[0], row[1], row[3], row[5], row[4]) 
				elif row[6] and row[0] == "spec_machine" and row[1] and row[3] and row[5]:
					car = SpecMachine(row[0], row[1], row[3], row[5], row[6])
				else:
					continue
				car_list.append(car)
			except:
				continue
	return car_list


if __name__ == "__main__":
	#csv_filename = sys.argv[1]
	csv_filename = "/media/anton/data/git/coursera_mipt_Python/week3/coursera_week3_cars.csv"
	print (get_car_list(csv_filename))