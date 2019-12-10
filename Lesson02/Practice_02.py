class Car:
    def __init__(self, num_of_doors, num_of_wheels, tires_type, color, brand):
        self._num_of_doors = num_of_doors
        self._num_of_wheels = num_of_wheels
        self._tires_type = tires_type
        self._color = color
        self._brand = brand

    def get_car_info(self):
        return dict(
            num_of_doors=self._num_of_doors,
            num_of_wheels=self._num_of_wheels,
            tires_type=self._tires_type,
            color=self._color,
            brand=self._brand
        )


class CarTruck(Car):
    def __init__(self, type_auto, max_weight,num_of_doors, num_of_wheels, tires_type, color, brand):
        self._type_auto = type_auto
        self._max_weight = max_weight
        super().__init__(num_of_doors, num_of_wheels, tires_type, color, brand)
    def get_car_info(self):
        # dict(x.items() + y.items())
        return print(dict(
            type_auto=self._type_auto,
            max_weight=self._max_weight
        ),
        super().get_car_info())

class PassengerCar(Car):
    def __init__(self, type_auto, comfort_level, num_of_doors, num_of_wheels, tires_type, color, brand):
        self._type_auto = type_auto
        self._comfort_level = comfort_level
        super().__init__(num_of_doors, num_of_wheels, tires_type, color, brand)

    def get_car_info(self):
        return print(dict(
            type_auto=self._type_auto,
            comfort_level=self._comfort_level
        ),super().get_car_info())


car1 = CarTruck('Truck', 2500, 4, 4, 'Winter', 'black', 'BMW')
car2 = PassengerCar('Sedan','SE',4,4,'Winter','red','Lada')
print(car1.get_car_info())
print(car2.get_car_info())