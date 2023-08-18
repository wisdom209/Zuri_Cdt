"""Module calculates best way to avoid obstructions"""
import math
from random import random


class CalculateBestWay():
    """Class that calculates best route for a machine"""
    __obstruction_time_limit = 60  # time limit in minutes for obstruction to be said to be impenetrable
    __SPEED_CONSTANT = 78

    def __init__(self, pointA: tuple, pointB: tuple) -> None:
        """Initialize the class"""
        self.__pointA = pointA
        self.__pointB = pointB
        self.__distance = self.__calculate_distance()
        self.__speed = None
        self.__expected_time = None

    @property
    def speed(speed):
        """getter for speed"""
        return speed

    @speed.setter
    def speed(self, value):
        """setter for speed"""
        self.__speed = value


    def __calculate_distance(self) -> float:
        """calculate distance"""
        x1 = self.__pointA[0]
        y1 = self.__pointA[1]
        x2 = self.__pointB[0]
        y2 = self.__pointB[1]

        distance_squared = math.pow(y1 - y2, 2) + math.pow(x1 - x2, 2)

        distance = math.pow(distance_squared, 0.5)

        return distance

    def check_for_obstructions(self) -> str:
        """checks if machine encounters an obstruction"""
        if self.__speed is None:
            return "Speed of the machine must be supplied"

        self.__expected_time = self.__distance / self.__speed   # get the expected time
        time_taken = (random() * (self.__expected_time + 180))  # simulate time taken


        if (time_taken > self.__expected_time + self.__obstruction_time_limit):
            return f"""
                    [*] There is an impenetrable obstruction

                    pointA = {self.__pointA}
                    pointb = {self.__pointB}

                    it should take {round(self.__expected_time, 1)}mins to go from
                    pointA to pointB but it took {round(time_taken,1)}mins which is 
                    {round(self.__obstruction_time_limit, 1)}mins more than the expected time.
                    """

        if (time_taken > self.__expected_time):
            return f"""
                    [*] There is an obstruction

                    pointA = {self.__pointA}
                    pointb = {self.__pointB}

                    it should take {round(self.__expected_time, 1)}mins to go from
                    pointA to pointB but it took {round(time_taken, 1)}mins
                    """

        return f"""
                [*] There is no obstruction

                pointA = {self.__pointA}
                pointb = {self.__pointB}

                it should take {round(self.__expected_time, 1)}mins to go from
                pointA to pointB but it took {round(time_taken,1)}mins.
                """
