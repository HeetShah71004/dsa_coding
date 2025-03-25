class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        def check(intervals):
            intervals.sort()
            
            sections = 0
            max_end = intervals[0][1]
            
            for start, end in intervals:
                if max_end <= start:
                    sections += 1
                max_end = max(max_end, end)
                
            return sections >= 2
        
        x_intervals = [[rect[0], rect[2]] for rect in rectangles]
        y_intervals = [[rect[1], rect[3]] for rect in rectangles]
        
        return check(x_intervals) or check(y_intervals)

# Test cases

n = 5
rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

print(Solution().checkValidCuts(n, rectangles))   # Output: True

