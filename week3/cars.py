import csv, os, sys

class CarBase:
   def __init__(self, car_type, brand, photo_file_name, carrying):
      self.brand = brand
      self.photo_file_name = photo_file_name
      self.carrying = carrying
      self.car_type = car_type

   def get_photo_file_ext(self):
      return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
   def __init__(self, passenger_seats_count):
      self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
   def __init__(self, body_whl):
      body_length, body_width, body_height = body_whl.split("x") or 0, 0, 0
      self.body_length = int(body_length)
      self.body_width = int(body_width)
      self.body_height = int(body_height) 
      
   def get_body_volume(self):
      return self.body_length * self.body_width * self.body_height

class SpecMachine(CarBase):
   def __init__(self, extra):
      self.extra = extra


def get_car_list(csv_filename):
   car_list = []
   with open(csv_filename) as csv_fd:
      reader = csv.reader(csv_fd, delimiter=';')
      next(reader)  # пропускаем заголовок
      for row in reader:
         car_list.append(row)
   return car_list
   
if __name__ == "__main__":
   csv_filename = sys.argv[1]
   car_list = get_car_list(csv_filename)
   for raw in car_list
