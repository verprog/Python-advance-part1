class Vehicle:
    # slots !!!
    # vehicle_type = 'Car'
    def __init__(self, num_of_doors, num_of_wheels, brand):
        self._num_of_doors = num_of_doors
        self._num_of_wheels = num_of_wheels
        self._brand = brand

    def  get_brand(self):
        return self._brand

    def  get_car_info(self):
        return dict(
                num_of_doors=self._num_of_doors,
                num_of_wheels=self._num_of_wheels
        )

    def  move(self):
        print('Moving')
class Car(Vehicle):

    def __init__(self, num_of_doors, num_of_wheels, brand, max_weight):
        self.max_weight = max_weight
        super().__init__(num_of_doors, num_of_wheels, brand)
        self.__engine = 'V-8'

    def  get_engine(self):
        return self.__engine

    def set_engine(self, value):
        if type!= str:
            raise Exception('Wrong type')
        self.__engine = value

    def _change_oil(self):
        print('Changing oil')

    def transport_smth(self, weight, thing):
        print(f'Transporting {thing}. The weight is {weight}')

    def __str__(self):
        return self.get_brand()


car = Vehicle(4,4,'BMW')
car.move()
# print(car.num_of_wheels)
# print(car.brand)
# print(car.num_of_doors)
# print(car.vehicle_type)

# car.vehicle_type = 'Truck'
# print(car.vehicle_type)
# print(Vehicle.vehicle_type)
car.new_variable = 100
print(car.new_variable)

print('*' * 30)

car1 = Car(4,4,'Mercedes', 400)
car1.transport_smth(200,'Animals')
print(car1.move())

print('*' * 30)
print(car1.get_car_info())

print('*' * 30)
print(dir(car1))
print(car1)