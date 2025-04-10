# src/simulator.py

from field import Field
from car import Car

class Simulaitor: 
    def __init__(self, field_width, field_heights, car_data_list):
        """
        car_data_list: list of dicts: { 'car': Car, 'commands': 'FFL' }
        """
        self.field = Field(field_width, field_heights)
        self.car_data = car_data_list
        self.positions = {}  # not using this now, maybe later if need to track

    def run(self):
        steps_max = max(len(c['commands']) for c in self.car_data)

        for step in range(steps_max):
            curr_posit = {}  # use this to for tracking next time in

            for data in self.car_data:
                car = data['car']
                commands = data['commands']

                if not car.active or step >= len(commands):
                    continue  # car already dead or no command left to start

                command = commands[step]

                if command == 'L':
                    car.rotate_left()
                elif command == 'R':
                    car.rotate_right()
                elif command == 'F':
                    next_x, next_y = car.move_forward()

                    # check if mov is valid insde feild
                    if not self.field.is_within_bounds(next_x, next_y):
                        continue  # skipping this move 

                    # collisiion checking here
                    for other in self.car_data:
                        if other == data or not other['car'].active:
                            continue
                        ox, oy, _ = other['car'].get_position()
                        if next_x == ox and next_y == oy:
                            print(f"- {car.name}, collides with {other['car'].name} at ({next_x},{next_y}) at step {step + 1}")
                            print(f"- {other['car'].name}, collides with {car.name} at ({next_x},{next_y}) at step {step + 1}")
                            car.active = False
                            other['car'].active = False
                            break
                    else:
                        # okay no colliseion, update posit
                        car.update_position(next_x, next_y)

        # Print final positons of cars that alive
        print("\nAfter simulation, the result is:")
        for data in self.car_data:
            car = data['car']
            if car.active:
                print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
