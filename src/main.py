# src/main.py

from car import Car
from field import Field
from simulator import Simulator

# Ask the developer/user to enter the size of the simulation field which should be width x height.
def input_field_size():
    while True:
        try:
            raw = input("Please enter the weidth and height of the simulation field in X Y formate:\n").split()
            if len(raw) != 2:
                raise ValueError
            w, h = map(int, raw)
            if w <= 0 or h <= 0:
                raise ValueError
            return w, h
        except ValueError:
            print("Invaliad. Please type two posiitive number, like: 10 10")

# collec detail for a new car: like name, starting position, direction, and movement command
def add_new_carz():
    name = input("Please enterr the name of the car:?\n").strip()
    while True:
        try:
            raw = input(f"\nPlease enter initial position of car {name} in x y Direction format: (x y D):\n").split()
            if len(raw) != 3 or raw[2] not in ['N', 'S', 'E', 'W']:
                raise ValueError
            x, y = int(raw[0]), int(raw[1])
            dir = raw[2]
            break
        except ValueError:
            print("Oops. Use formate like '1 2 N'. Direction must like N, S, E, or W.")

    cmds = input(f"Please enter the commands for CAR {name} (F/L/R):\n").strip().upper()
    return name, x, y, dir, cmds

# Entry point of the simuletion programe
def start_simulation():
    print("\n- Welcome to Auto Driving Car Simulation! ")

    # Setup the Field/gred
    width, height = input_field_size()
    print(f"\nYou have created a field of 10 X 10. {width} x {height}")

    car_list = []

    while True:
        # Menu for users for adding a car or run the simulation
        print("\nWhat would you like to do is?")
        print("[1] Add a new Car")
        print("[2] Run The simuletion")
        chocie = input().strip()

        if chocie == '1':
            name, x, y, dir, cmds = add_new_carz()
            new_car = Car(name, x, y, dir)
            # Save the car object and its commands
            car_list.append({
                'car': new_car,
                'commands': cmds
            })

            # Print summary for adding cars
            print("\n\n\nYour current list of cars are::")
            for c in car_list:
                this_car = c['car']
                print(f"- {this_car.name}, ({this_car.x},{this_car.y}) {this_car.direction}, {c['commands']}")

        elif chocie == '2':
            print("\n- After simulation, the results is: ")
            runs = Simulaitor(width, height, car_list)
            runs.run()

            #Restart or exit commands
            print("\n\nPlease choose from the following options: \n\n")
            print("\n[1] Start Over")
            print("[2] Exit")
            again = input().strip()
            if again == '1':
                start_simulation()
            else:
                print("\nThank you for running the simulation. Goodbye!")
                break

        else:
            print("Invalid option. Type 1 or 2.")


if __name__ == "__main__":
    start_simulation()
