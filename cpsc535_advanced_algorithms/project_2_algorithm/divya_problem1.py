from typing import List

def optimizing_product_lines(durations: List[int], stations: int):
    low = max(durations) # a station will not have duration less then maximum of all durations
    high = sum(durations) # a station will not have duration more then sum of all durations
    # Binary search to find  the optimal maximum duration a single station can have after the duration have been assigned.
    # Repeat until low meets high
    while low < high:
        no_of_station_required = 1 # Start with single station
        current_station_duration = 0 
        mid = (low + high) // 2 # Maximum duration a station can have

        for duration in durations:
            # If it is more then mid then we need to add more station in production line
            if current_station_duration + duration > mid:
                no_of_station_required += 1 # Increase the number of station
                current_station_duration = duration # Duration for the current station
                if no_of_station_required > stations: # If it exceeds from given number of station then break
                    break
            # If adding duration is less then mid then update duration at current station
            else:
                current_station_duration += duration
        # If no of station required exceeded then given station, then we need to add more time per station
        if no_of_station_required > stations:
            low = mid + 1
        
        # Otherwise can handle within the number of stations
        else:
            high = mid
    # low is the maximum duration duration taken by a single station in production line
    return low

if __name__ == '__main__':
    durations = [15, 15, 30, 30, 45]
    stations = 3
    result = optimizing_product_lines(durations=durations, stations=stations)
    print(f'Maximum duration: {result}')

               



