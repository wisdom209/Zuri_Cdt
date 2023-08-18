# CalculateBestWay Module

The purpose of this task is to demonstrate OOP concepts

## Requirements

To successfully run this taks, the following requirements must be met:

- Python (version 3.6 or higher)

## Usage

An example has been provided in `main.py` module which shows how it can be used

Run this example in your terminal like this: `python3 main.py`


## Explanation

The `CalculateBestWay` class is designed to handle the detection of obstructions and determine if they are impenetrable. It utilizes object-oriented programming principles to ensure code reusability. It also demonstrates encapsulation as attributes not needed outside the class are made private.

The class provides the following methods:

- `calculate_distance()`: Calculates the distance between two points. A private function not accessible outside the class where it is defined

-  `check_for_obstructions()`: Checks for obstructions based on the provided machine speed, distance, and expected time and prints out the result in this format:

```
                    [*] There is an impenetrable obstruction

                    pointA = (53.5872, -2.4138)
                    pointb = (53.474, -2.2388)

                    it should take 78.0mins to go from
                    pointA to pointB but it took 164.1mins which is 
                    60mins more than the expected time.
```
Based on the text above, the module calculates the expected time to travel from point A to point B as 78 minutes. Since this expected time is significantly less than the time taken which is 164.1mins and because this time is 60 minutes more than the expected time, it indicates that there is an obstruction and it is considered impenetrable.

Please note that the module assumes that there is another module to calculate the time taken from one distance to another, however the results are simulated in this module.

## Assumptions

The following assumptions are made in the implementation of this module:

- The time duration module has already been developed and can simulate the time taken from one distance to another.
- The module has access to the speed of the digging machine which will be supplied.
- The speed, distance, and time taken are not hardcoded into the module since point A and point B are not fixed and can vary.

