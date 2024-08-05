import random
import time
import os


class Racer:
    """
    Racer class to represent a bus in
    """

    def __init__(self, name: str, repr: str):
        """
        Initialize the Racer class
        :param name: str: Name of the bus
        :param repr: str: Representation of the bus
        """
        self.name = name
        self.repr = repr
        self.position = 0

    def move(self, inc: int) -> int:
        """
        Move the bus by the given increment
        :param inc: int: Increment by which the bus should move
        :return: int: The new position of the bus
        """
        self.position += inc

    def is_finished(self, length: int) -> bool:
        """
        Check if the bus has finished
        :param length: int: The length
        :return: bool: True if the bus has finished, False otherwise
        """
        return self.position >= length

    def __str__(self):
        """
        String representation of the bus
        :return: str: The string representation of the bus
        """
        return f"{self.repr} {self.name}"


class Race:
    """
    Race class to represent a race between buses in a road with a given length and velocity of the buses
    """

    def __init__(self, length, buses: list[Racer], velocity: float = 0.25):
        """
        Initialize
        :param length: int: The length of the road
        :param buses: list[Racer]: The list of buses
        :param velocity: float: The velocity of the buses
        """
        self.length = length
        self.buses = buses
        self.velocity = velocity
        self.podium = []
        self.walls = ["="] * (self.length + 2)
        self.sep = ["-"] * (self.length + 2)
        self.medalls = ["🥇", "🥈", "🥉"]

    def change_position(self, bus: Racer) -> list[str]:
        """
        Change the position of the bus
        :param bus: Racer: The bus
        :return: list[str]: The new position of the bus
        """
        road = [" "] * self.length
        if bus.position < self.length:
            road[bus.position] = bus.repr
            return road
        road[-1] = bus.repr
        return road

    def print_road(self):
        """
        Print the road in the terminal with the buses in their respective positions on the road
        """
        os.system("cls" if os.name == "nt" else "clear")
        lanes = []
        # Create a lane for each bus and add it to the lanes
        for bus in self.buses:
            road = self.change_position(bus)
            lanes.append(road)

        print("".join(self.walls))
        print("".join(self.sep))
        for road in lanes:
            print("|" + "".join(road))
            print("".join(self.sep))
        print("".join(self.walls))

    def start_race(self):
        """
        Start the race
        """
        # Print the initial formation of the buses
        self.print_road()
        time.sleep(self.velocity)
        # Move the buses until all buses have finished
        while True:
            [bus.move(random.randint(1, 3)) for bus in self.buses]
            self.print_road()
            time.sleep(self.velocity)

            for bus in self.buses:
                if bus.is_finished(self.length):
                    self.add_to_podium(bus)

            if all([bus.is_finished(self.length) for bus in self.buses]):
                break
        # Print the winner and the podium
        podium = self.podium[:3]
        self.print_winner(podium[0])
        self.print_podium(podium)

    def add_to_podium(self, bus: Racer) -> None:
        """
        Add the bus to the podium
        :param bus: Racer: The bus
        """
        if bus not in self.podium:
            self.podium.append(bus)

    def print_winner(self, winner: Racer) -> None:
        """
        Print the winner
        :param winner: Racer: The winner
        """
        print(f"\n 🎊🎉🎊 The winner is {winner} 🏆🍾  🎊🎉🎊")

    def print_podium(self, podium: list[Racer]) -> None:
        """
        Print the podium
        :param podium: list[Racer]: The podium
        """
        print("Podium:")
        for i, bus in enumerate(podium):
            print(f"{i+1}. {bus.repr} {bus.name} {self.medalls[i]}")


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
