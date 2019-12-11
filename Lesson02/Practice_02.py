# Задание №1
print('Задание №1')
class Car:
    def __init__(self, num_of_doors, num_of_wheels, tires_type, color, brand):
        self._num_of_doors = num_of_doors
        self._num_of_wheels = num_of_wheels
        self._tires_type = tires_type
        self._color = color
        self._brand = brand

    def _get_car_info(self):
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

    def _get_car_info(self):
        inf = dict(
            type_auto=self._type_auto,
            max_weight=self._max_weight
        )
        inf.update(super()._get_car_info())
        return inf


class PassengerCar(Car):
    def __init__(self, type_auto, comfort_level, num_of_doors, num_of_wheels, tires_type, color, brand):
        self._type_auto = type_auto
        self._comfort_level = comfort_level
        super().__init__(num_of_doors, num_of_wheels, tires_type, color, brand)

    def _get_car_info(self):
        inf = dict(
            type_auto=self._type_auto,
            comfort_level=self._comfort_level
        )
        inf.update(super()._get_car_info())
        return inf


car1 = CarTruck('Truck', 2500, 4, 4, 'Winter', 'black', 'BMW')
car2 = PassengerCar('Sedan','SE',4,4,'Winter','red','Lada')
print(car1._get_car_info())
print(car2._get_car_info())


print('*' * 30)
# Задание №2
print('Задание №2')

class Shop:
    quantity_total_sale = 0

    def __init__(self, shop_name, quantity_sale_wares):
        self._shop_name = shop_name
        self._quantity_sale_wares = quantity_sale_wares
        Shop.quantity_total_sale += quantity_sale_wares

    def howquantity(self):
        print('Было реализовано {0:d} еденицы товаров.'.format(Shop.quantity_total_sale))


shop1 = Shop('Aliexpress',33)
shop2 = Shop('Marichka',13)

shop1.howquantity()


print('*' * 30)
# Задание №3
print('Задание №3')

class Point:

    def __init__(self, point_x, point_y, point_z):
        self._point_x = point_x
        self._point_y = point_y
        self._point_z = point_z

    def _get_result(self):
        res = [self._point_x, self._point_y, self._point_z]
        return res



    def __add__(self, other):
        return Point(self._point_x + other._point_x, self._point_y + other._point_y, self._point_z + other._point_z)

    def __sub__(self, other):
        return Point(self._point_x + (-other._point_x), self._point_y + (-other._point_y), self._point_z + (-other._point_z))

    def __mul__(self, other):
        return Point(self._point_x * other._point_x, self._point_y * other._point_y, self._point_z * other._point_z)

    def __truediv__(self, other):
        try:
            return Point(self._point_x / other._point_x, self._point_y / other._point_y, self._point_z / other._point_z)
        except ZeroDivisionError:
            print('Деление на ноль')

    def _get_result(self):
        res = [self._point_x, self._point_y, self._point_z]
        return res


point1 = Point(1, 2, 3)
point2 = Point(1, 2, 3)

result = point1 * point2

print(result._get_result())
