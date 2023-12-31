
from Calculate_Best_Way import CalculateBestWay

# define the points
pointA = (53.5872, -2.4138)
pointB = (53.474, -2.2388)

# create an instance of the class with the points
calculator_instance = CalculateBestWay(pointA, pointB)  # in miles

# set the seed of the machine
calculator_instance.speed = 0.00267		# miles/sec

# store the result of the function that checks for obstructions
result = calculator_instance.check_for_obstructions()

# print the result
print(result)
