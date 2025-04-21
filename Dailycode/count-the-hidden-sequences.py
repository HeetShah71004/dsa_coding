class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        x=1
        max_x,min_x=x,x

        for diff in differences:
            x+=diff
            max_x=max(max_x,x)
            min_x=min(min_x,x)
        ranger=max_x-min_x
        return max((upper-lower+1)-ranger,0)

# Test cases
differences = [1,-3,4]
lower = 1
upper = 6
solution = Solution()
result = solution.numberOfArrays(differences, lower, upper)
print(result)  # Output: 2