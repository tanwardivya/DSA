class CarFleet:
    def car_fleet(self,target:int,position:list[int],speed:list[int])->int:
#creating an array of pairs and iterate through the position and speed array simultaneously, i can do that with zip  
        pair = [[p,s] for p,s in zip(position,speed)]  
        print("Pairs:", pair)

        #sorting the pairs in descending order of position
        sorted_pairs = sorted(pair,reverse = True)
        print("Sorted_pairs:", sorted_pairs)

        stack = []
# This sorts the pairs in descending order of position. The [::-1] reverses the sorted list.       
        for p,s in sorted(pair)[::-1]:
            
#  This calculates the time taken for each car to reach the target and adds it to the stack.           
            stack.append((target-p)/s)
# This checks if the current car (the last in the stack) will catch up with the 
# car in front of it before reaching the target. If so, it removes the current 
# car from the stack, effectively merging it into the fleet of the car in front.

# this first check the length of te stack is greater than and equal to 2, if top
# of the stack reaches the destination before the one that's ahead of it at 
# index [-2] like if the time of it is less than the next one that must mean 
# they collide that must mean we have to pop from the top of the stack an by 
# doing that we're decreasing the number of car fleets if we don't pop then we 
# leave it as it is.

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        print("final_stack:", stack)
        return len(stack )

def main():
    cf = CarFleet()
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    result = cf.car_fleet(target,position,speed)
    print("Fleet_count Result:", result)

    result1 = cf.car_fleet(10,[3],[3])
    print("Fleet_count Result:", result1)

    result2 = cf.car_fleet(100,[0,2,4],[4,2,1])
    print("Fleet_count Result:", result2)
   

if __name__ == "__main__":
    main()

#explaination:
#Process:
# Create Pairs of Position and Speed:

# Pairs: [[10, 2], [8, 4], [0, 1], [5, 1], [3, 3]]
# Sort Pairs in Descending Order of Position:

# Sorted Pairs: [[10, 2], [8, 4], [5, 1], [3, 3], [0, 1]]
# Calculate Time to Reach Target and Use Stack:

# For each car, calculate the time to reach the target: (target - position) / speed.
# Add this time to the stack.
# If the time for a car is less than or equal to the time for the car in front of it, it will join that fleet.
#Step 4: Iterate Through Sorted Pairs with Popping Logic
# We have the sorted pairs: [[10, 2], [8, 4], [5, 1], [3, 3], [0, 1]]. We'll calculate the time for each car to reach the target and use the stack to determine if cars form a fleet.

# Car at Position 10 with Speed 2

# Time = (12 - 10) / 2 = 1
# Stack = [1]
# Car at Position 8 with Speed 4

# Time = (12 - 8) / 4 = 1
# Stack = [1, 1]
# Since the time for the car at position 8 (1) is equal to the time for the car at position 10 (1), they form a fleet. We pop the last element (representing the car at position 8) because it joins the fleet of the car at position 10.
# Updated Stack = [1]
# Car at Position 5 with Speed 1

# Time = (12 - 5) / 1 = 7
# Stack = [1, 7]
# The car at position 5 does not catch up to the fleet formed by cars at positions 10 and 8, so it remains a separate fleet.
# Car at Position 3 with Speed 3

# Time = (12 - 3) / 3 = 3
# Stack = [1, 7, 3]
# The car at position 3 does not catch up to the car at position 5 (since 3 < 7), so it remains a separate fleet.
# Car at Position 0 with Speed 1

# Time = (12 - 0) / 1 = 12
# Stack = [1, 7, 3, 12]
# The car at position 0 does not catch up to any other car, so it remains a separate fleet.
# Popping Logic Explanation
# The popping step is crucial for determining whether a car joins an existing fleet or remains a separate fleet. When we add a car's time to the stack, we check if this time is less than or equal to the time of the car in front of it in the stack. If it is, this means the car will catch up and join the fleet of the car in front of it, and we pop the last element from the stack to represent this merging.

# In this example, the only merging happens between the cars at positions 10 and 8, as they both have the same time to reach the target. For the other cars, since each one has a greater time to reach the target than the one in front of it, they do not merge, and no further popping occurs.

# Final Stack and Fleet Count
# Final Stack: [1, 7, 3, 12]
# Fleet Count: 4 (Initially, it seems like 4, but since the first two elements represent the same fleet, the actual count is 3).
# Thus, there are 3 distinct fleets: one consisting of cars from positions 10 and 8, one from position 0, and one each from positions 5 and 3.




