class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        
        merged_meetings = []
        for meeting in meetings:
            if not merged_meetings or meeting[0] > merged_meetings[-1][1]:
                merged_meetings.append(meeting)
            else:
                merged_meetings[-1][1] = max(merged_meetings[-1][1], meeting[1])
        
        meeting_days_count = 0
        for start, end in merged_meetings:
            meeting_days_count += end - start + 1
        
        return days - meeting_days_count

# Test cases:-

days = 10
meetings = [[5,7],[1,3],[9,10]]

print(Solution().countDays(days, meetings))  # Output: 2