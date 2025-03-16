class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        left = 1
        right = min(ranks) * cars * cars 
        
        def can_repair_all(time):
            total_cars_repaired = 0
            for rank in ranks:
                cars_repaired = int((time / rank) ** 0.5)
                total_cars_repaired += cars_repaired
                if total_cars_repaired >= cars:
                    return True
            return False
        
        while left < right:
            mid = (left + right) // 2
            if can_repair_all(mid):
                right = mid
            else:
                left = mid + 1
                
        return left



# Test cases
ranks = [4,2,3,1]
cars = 10


print(Solution().repairCars(ranks, cars)) 

        