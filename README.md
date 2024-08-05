# Bus Race Simulation
## Overview
This project is a simple simulation of a bus race. The program features a race between several buses along a virtual road, with each bus moving randomly in each iteration until one or more buses finish the race. The race status, including the positions of the buses, is updated and displayed in the terminal throughout the simulation. The top three buses are then displayed on the podium with medals.

![imagen](https://github.com/user-attachments/assets/0d6aab6a-3e4c-4d97-8e19-bae72810469c)

Classes
### Racer

Represents a bus in the race.

- Attributes:
    name (str): The name of the bus.
    repr (str): A character representation of the bus (e.g., "🔵").
    position (int): The current position of the bus on the road.

- Methods:
    __init__(name: str, repr: str): Initializes a Racer instance with a name and representation.
    move(inc: int) -> int: Moves the bus forward by the specified increment.
    is_finished(length: int) -> bool: Checks if the bus has reached or exceeded the finish line.
    __str__() -> str: Returns a string representation of the bus.

### Race

Manages the racing simulation between buses.

- Attributes:
    length (int): The length of the road.
    buses (list[Racer]): A list of Racer instances participating in the race.
    velocity (float): The delay (in seconds) between each iteration of the race.
    podium (list[Racer]): A list of buses that have finished the race.
    walls (list[str]): A list representing the walls of the road for display purposes.
    sep (list[str]): A list representing the separators of the road for display purposes.
    medalls (list[str]): A list of medal emojis used for the podium.

- Methods:
    __init__(length: int, buses: list[Racer], velocity: float = 0.25): Initializes a Race instance with road length, list of buses, and velocity.
    change_position(bus: Racer) -> list[str]: Returns a list representing the road with the bus at its current position.
    print_road(): Clears the terminal and prints the current state of the road with all buses.
    start_race(): Starts the race, moving buses and updating the display until all buses have finished.
    add_to_podium(bus: Racer): Adds a bus to the podium list if it’s not already there.
    print_winner(winner: Racer): Prints the winner of the race.
    print_podium(podium: list[Racer]): Prints the podium with the top three buses and their respective medals.

## Usage

1. Initialize the Race:

The data dictionary defines the road length and the list of buses. Each bus is specified with a name and a repr (character representation). The Race class is then instantiated using this data.

2. Start the Race:

Call the start_race() method on the Race instance to begin the simulation. The method will print the initial state, update the positions of the buses in each iteration, and display the final results.

## Example:

    if __name__ == "__main__":

    data = {
        "length": 100,
        "buses": [
            {"name": "Speedy", "repr": "🔵"},
            {"name": "Slowpoke", "repr": "⚪"},
            {"name": "Average", "repr": "🟣"},
            {"name": "Blazing", "repr": "🔴"},
            {"name": "Turtle", "repr": "🟡"},
        ],
    }

    buses = [Racer(**bus) for bus in data["buses"]]

    race = Race(data["length"], buses)
    race.start_race()

https://github.com/user-attachments/assets/f6110454-b5f6-49b6-a870-50cc45796d67



## Dependencies

- Python 3.6+: The code is compatible with Python 3.6 and above.
- os and time libraries: Used for terminal operations and timing.
- random library: Used for generating random movement increments.

## Notes
- The terminal screen is cleared and updated on each iteration of the race for better visualization.
- The velocity attribute controls the delay between updates and can be adjusted to speed up or slow down the simulation.

Feel free to modify the data dictionary to change the race parameters and experiment with different configurations!
