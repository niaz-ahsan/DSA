# Given an unsorted array AA, the maximum sum subarray is the subarray (contiguous elements) from AA for which the sum of the elements is maximum. In this challenge, we want to find the sum of the maximum sum subarray.

# O(n) Time & O(1) Space --> Kadane's algorithm
def solve(arr):
    max_sum = float("-inf")
    curr_sum = 0
    for elem in arr:
        curr_sum = max(curr_sum + elem, elem)
        max_sum = max(curr_sum, max_sum)
    return max_sum    

if __name__ == "__main__":
    arr = [1, 7, -2, -5, 10, -1]
    print(solve(arr))