"""task4"""


class Car:
    """Клас, що описує автомобіль"""
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model}, {self.year} року. Ціна:{self.price}"


class CarDealership:
    """Клас, що описує автосалон"""
    def __init__(self):
        """Ініціалізація словника з данними про доступні авто"""
        self.available_cars = {}

    def add_car(self, car_id, car):
        """Функція додавання авто до списку доступних"""
        self.available_cars[car_id] = car

    def sell_car(self, car_id):
        """Функція продажу та видалення авто з доступних"""
        if car_id in self.available_cars:
            car = self.available_cars.pop(car_id)
            print(f"Автомобіль {car.brand} {car.model} {car.year} продано.")
        else:
            print("За даним ідентифікатором нічого не знайдено.")


car1 = Car("Toyota", "Camry", 2014, 15000)
car2 = Car("Toyota", "Hilux", 2018, 18500)
car3 = Car("Ford", "F150", 2019, 20000)


# print(car1)


dealership = CarDealership()


dealership.add_car(1, car1)
dealership.add_car(2, car2)
dealership.add_car(3, car3)


dealership.sell_car(2)
dealership.sell_car(4)
