class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor request. The floor is out of range.")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            self.print_current_floor()

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            self.print_current_floor()
    def print_current_floor(self):
        print(f"Elevator is now on floor {self.current_floor}")
if __name__ == "__main__":
    elevator = Elevator(bottom_floor=1, top_floor=10)
    elevator.go_to_floor(5)
    elevator.go_to_floor(1)

