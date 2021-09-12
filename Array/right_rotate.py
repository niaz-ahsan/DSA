# Implement a function rightRotate(int arr[], int size) which takes an array arr and rotate it right by 1. This means that the right-most elements will appear at the left-most position in the array.

# O(n) Time & O(n) Space
def solve(arr, rotation):
    output = [None] * len(arr)
    for index, elem in enumerate(arr):
        new_index = index + rotation
        size = len(arr)
        if new_index >= size:
            new_index %= size
        output[new_index] = elem
    return output    


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    rotation = 7
    print(solve(arr, rotation))
