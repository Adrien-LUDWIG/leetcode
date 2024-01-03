class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        laser_count = 0
        last_device_count = 0

        for row in bank:
            device_count = row.count("1")

            if device_count:
                laser_count += last_device_count * device_count
                last_device_count = device_count
        
        return laser_count
