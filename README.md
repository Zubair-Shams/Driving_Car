# Auto Driving Cars Simulations

This project will simulates cars moving in a rectangular grid box, as like that how autonomous driving systems can work and move. The goal for this task to create a basic simulation where multiple cars can move around in box/grid, follow the instructions, and detect collisions when it hit to eah other.

## How its work

-This project will starts by asking the user/developer to enter the field size. like box/grid size of 10 10
-After that, user will add one or more cars by giving them a name, starting position, direction (N, S, E, or W) which shows the direction of norht, south, east and west, with a command string.

-These commands string can contains:
  -F = move forward one step
  -L = turn left
  -R = turn right

-Once all car are added, the simulations run. Each cars process one command per steps. If two cars end up in the same cell at the same step, they are marked as collided and stop.

## Running the project

1. Make sure you have Python installed.
2. Open terminal and go to the `src` folder.
3. Run the program with:

```bash
python main.py
