from collections import Counter

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Map garbage trucks type to minutes of garbage collecting and
        # travelling from one house to another
        trucks_collecting_time = {'M': 0, 'P': 0, 'G': 0}
        trucks_travelling_time = {'M': 0, 'P': 0, 'G': 0}

        # Keeps track of the travel time from the beginning to the current house
        cumulative_travel_time = 0

        # Adjust size to be enable to zip
        travel.append(0)

        for curr_house_garbage, travel_time_to_next_house in zip(garbage, travel):
            # Count garbage by type
            garbage_count = Counter(curr_house_garbage)

            # Update collecting and travel time for trucks needed at this house
            for garbage_type, garbage_type_count in garbage_count.items():
                trucks_collecting_time[garbage_type] += garbage_type_count
                trucks_travelling_time[garbage_type] = cumulative_travel_time
            
            cumulative_travel_time += travel_time_to_next_house

        return sum(trucks_collecting_time.values()) + sum(trucks_travelling_time.values())
            



        