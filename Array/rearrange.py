# Implement a function reArrange(int arr[], int size) which takes an array arr and its size as input and rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right.

def find_left_pointer_position(arr, p):
    while arr[p] < 0:
        p += 1
    return p

def find_right_pointer_position(arr, p):
    while arr[p] >= 0:
        p -= 1
    return p        

def swap(l, r):
    arr[l], arr[r] = arr[r], arr[l]

# O(n) Time & O(1) Space
def solve(arr):
    left_pointer = 0
    right_pointer = len(arr) - 1
    while left_pointer < right_pointer:
        left_pointer = find_left_pointer_position(arr, left_pointer)
        right_pointer = find_right_pointer_position(arr, right_pointer)
        if left_pointer < right_pointer:
            swap(left_pointer, right_pointer)
    return arr        

if __name__ == "__main__":
    arr = [10,-1,20,4,5,-9,-6]
    print(solve(arr))