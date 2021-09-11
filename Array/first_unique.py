#Implement a function, findFirstUnique(int arr[], int size) which takes an array and its size as input and returns the first unique integer in the array. The function returns -1 if no unique number is found.

# O(n) Time & Space
def solve_opt(arr):
    tracker = {}
    for i in range(len(arr)):
        if arr[i] in tracker:
            del tracker[arr[i]]
        else:
            tracker[arr[i]] = i
    min_index = float("inf")
    output = None
    for k,v in tracker.items():
        if v < min_index:
            min_index = v
            output = k
    return output        


# O(n^2) Time & O(1) Space
def solve(arr):
    for i in range(len(arr)):
        found = False
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] == arr[j]:
                found = True
                break
        if not found:
            return arr[i] 
    return -1                   

if __name__ == "__main__":
    arr = [2,3,9,2,3,6]
    #arr = [4,5,1,2,0,4]
    print(solve_opt(arr))
