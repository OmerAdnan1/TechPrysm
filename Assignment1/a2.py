
# Implement flow of a factory pattern for the creation of a car, in which there are different objects like seats, engine, doors, multimedia, suspension, electrical system etc. Ensuring only a single object of the Car Factory is ever available, keep track of cars produced by the factory and provide an interface to get a list of all those cars and their counts.
# Factory should help make a car with custom requirements for all mentioned components, with sensible defaults set.

from abc import ABC, abstractmethod
from datetime import datetime


class CarPart:
    def __init__(self, name, price, description):
        self.name: str = name
        self.price: float = price
        self.description: str = description

    def display(self):
        print("Part: ", self.name)
        print("Price: ", self.price)
        print("Description: ", self.description)

class Seat(CarPart):
    def __init__(self, name="Leather Seats", price=0.0, description="Leather Seats"):
        super().__init__(name, price, description)


class Engine(CarPart):
    def __init__(self, name="1.5L Petrol Engine", price=0.0, description="Petrol Engine"):
        super().__init__(name, price, description)


class Door(CarPart):
    def __init__(self, name="4 Doors", price=0.0, description="Standard Doors"):
        super().__init__(name, price, description)


class Multimedia(CarPart):
    def __init__(self, name="Basic Multimedia", price=0.0, description="Basic Multimedia System"):
        super().__init__(name, price, description)


class Suspension(CarPart):
    def __init__(self, name="Standard Suspension", price=0.0, description="Standard Suspension"):
        super().__init__(name, price, description)


class ElectricalSystem(CarPart):
    def __init__(self, name="Standard Electrical System", price=0.0, description="Standard Electrical System"):
        super().__init__(name, price, description)


class Car:
    _next_id = 1

    def __init__(self, model, engine, seats, doors, multimedia, suspension, electrical):
        self.id = Car._next_id
        Car._next_id += 1

        self.model = model
        self.engine = engine
        self.seats = seats
        self.doors = doors
        self.multimedia = multimedia
        self.suspension = suspension
        self.electrical = electrical
        self.produced_at = datetime.now()

    def __repr__(self):
        return (f"Car #{self.id} [{self.model}] "
                f"{self.engine}, {self.seats}, {self.doors}, "
                f"{self.multimedia}, {self.suspension}, {self.electrical}")

    def summary(self):
        return f"Car #{self.id} - {self.model} (produced {self.produced_at:%H:%M:%S})"


class CarFactory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._produced_cars = []
        self._initialized = True

    def create_car(self, model, engine=None, seats=None, doors=None,
                   multimedia=None, suspension=None, electrical=None):
        car = Car(
            model=model,
            engine=engine or Engine(),
            seats=seats or Seat(),
            doors=doors or Door(),
            multimedia=multimedia or Multimedia(),
            suspension=suspension or Suspension(),
            electrical=electrical or ElectricalSystem(),
        )
        self._produced_cars.append(car)
        return car


    def get_all_cars(self):
        return list(self._produced_cars)  # return a copy, protect internal state

    def get_total_produced(self):
        return len(self._produced_cars)


if __name__ == "__main__":
    factory1 = CarFactory()
    factory2 = CarFactory()
    print(f"factory1 is factory2 = {factory1 is factory2}")

    car1 = factory1.create_car("Sedan V1")

    custom_engine = Engine(name="2.0L Turbocharged Engine", price=2500.00, description="High performance turbo engine")
    car2 = factory1.create_car("Sports Coupe", engine=custom_engine)

    car3 = factory1.create_car("Sedan V1")

    print(f"\nTotal Cars Produced: {factory1.get_total_produced()}")

    print("\n--- All Produced Cars ---")
    for car in factory1.get_all_cars():
        print(car.summary())