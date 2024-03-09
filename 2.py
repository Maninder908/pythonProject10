import random

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance_traveled = 0

    def drive(self):
        self.distance_traveled += self.speed

    def get_status(self):
        return f"{self.name}: {self.distance_traveled} km"

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.speed += random.uniform(-5, 5)  # Random speed change
            car.drive()

    def print_status(self):
        print("\nRace Status:")
        for car in self.cars:
            print(car.get_status())
        print("-------------")

    def race_finished(self):
        for car in self.cars:
            if car.distance_traveled >= self.distance:
                return True
        return False


if __name__ == "__main__":

    cars = [Car(f"Car{i}", random.randint(120, 200)) for i in range(2, 14)]


    grand_demolition_derby = Race("Grand Demolition Derby", 8000, cars)


    hours = 0
    while not grand_demolition_derby.race_finished():
        if hours % 10 == 0:
            grand_demolition_derby.print_status()
        grand_demolition_derby.hour_passes()
        hours += 1


    grand_demolition_derby.print_status()
    print("Race finished in", hours, "hours.")





