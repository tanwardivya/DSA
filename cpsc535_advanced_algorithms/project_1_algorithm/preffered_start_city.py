"""To solve this problem, the algorithm can be designed as follows.

Start the from the first gas station and while moving to the next station stores the 
total fuel by multiplying mpg to the fuel available at current station and subtarcting the distance of next city.
Check whether there is deficit of fuel or not. If there is deficit then
add the value to deficit which was calculated till the previous gas station and update the start
position to next position and mark the capacity to zero since at the start of the drive car is empty tank.
Since, it's circular track the car moves until it reaches to the position it started. 
To avoid visting gas station multiple time, if sum of fuel available and fuel deficit is 
greater than or equal to zero then return the start position otherwise there is no valid preferred start position.
"""
from typing import List
class Solution:
    """Preferred Starting City Algorithm."""

    def preffered_starting_city(self,distance:List[int], fuel:List[int], mpg:int)-> int:
        """Returns the preffered starting city.

        Args:
            distance (List[int]): array of distance
            fuel (List[int]): array of fuel
            mpg (int): speed

        Returns:
            int: Preffered starting city index
        """
        start = 0  # Car starting position, let start from first position
        capacity = 0 #Initial capacity i.e. fuel available till now
        deficit = 0 # Deficit fuel till visiting next gas station
        length = len(distance) # Array length
        # Visiting each city 
        for current_index in range(length):
            # Calculate fuel available till 
            capacity += fuel[current_index] * mpg - distance[current_index]
            # Check whethere fuel is deficit or not
            if capacity < 0:
                #Update start the position to next position since current position will 
                # not be preffered start as the gas isn't enough to reach back to start point.
                start = current_index + 1 
                deficit += capacity #Update deficit till current gas station
                capacity = 0 #Set capcity to zero since at the start car is empty tank
        # After the loop ends, check whether sum of fuel available and deficit is 
        # greater or equal to zero, if yes then returns start position.
        if deficit + capacity >= 0: 
            return start
        # Preffered start city not found
        return -1

if __name__ == '__main__':
    distance = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    solution = Solution()
    result = solution.preffered_starting_city(distance, fuel, mpg)
    print(f"Unique starting city:{result}")

         
            

