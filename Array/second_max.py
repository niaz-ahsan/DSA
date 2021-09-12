#Implement a function findSecondMaximum(int arr[], int size) which takes an array arr and its size as input and returns the second maximum element in the array. If no such element found then return secondmax variable.

# O(n) Time & O(1) Space, more optimal as done in one traversal
def solve_opt(arr):
    greatest = second_greatest = float("-inf")
    for elem in arr:
        if elem > greatest:
           second_greatest = greatest
           greatest = elem
    return second_greatest        

# O(n) Time & O(1) Space
def solve(arr):
    greatest = float("-inf")
    for elem in arr:
        greatest = max(greatest, elem)
    diff = float("inf")
    output = None
    for elem in arr:
        curr_diff = greatest - elem
        if curr_diff > 0 and curr_diff < diff:
            diff = curr_diff
            output = elem
    return output        


if __name__ == "__main__":
    arr = [9,2,3,6]
    arr = [4,2,1,5,0]
    print(solve_opt(arr))