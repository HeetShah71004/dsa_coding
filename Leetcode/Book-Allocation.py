def is_valid(arr, n, m, max_allowed_pages):
    students = 1
    pages = 0

    for i in range(n):
        if arr[i] > max_allowed_pages:
            return False

        if pages + arr[i] <= max_allowed_pages:
            pages += arr[i]
        else:
            students += 1
            pages = arr[i]

    return students <= m

def allocate_books(arr, n, m):
    if m > n:
        return -1

    total_pages = sum(arr)
    start, end = 0, total_pages
    ans = -1

    while start <= end:
        mid = start + (end - start) // 2

        if is_valid(arr, n, m, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans

# Example usage
arr = [2, 1, 3, 4]
n = 4
m = 2

print(allocate_books(arr, n, m))  # Output: 6
