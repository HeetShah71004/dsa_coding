class Solution:
    def singleNonDuplicate(self, A):
        n = len(A)
        
        if n == 1:
            return A[0]

        st, end = 0, n - 1

        while st <= end:
            mid = st + (end - st) // 2

            if mid == 0 and A[0] != A[1]:
                return A[0]
            if mid == n - 1 and A[n - 1] != A[n - 2]:
                return A[n - 1]
            if A[mid - 1] != A[mid] and A[mid] != A[mid + 1]:
                return A[mid]

            if mid % 2 == 0:  # even index
                if A[mid - 1] == A[mid]:  # pair is to the left
                    end = mid - 1
                else:  # pair is to the right
                    st = mid + 1
            else:  # odd index
                if A[mid - 1] == A[mid]:  # single is to the right
                    st = mid + 1
                else:  # single is to the left
                    end = mid - 1

        return -1

sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))  # Output: 2
print(sol.singleNonDuplicate([3,3,7,7,10,11,11]))   # Output: 10
