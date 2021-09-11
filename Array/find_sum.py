# Find 2 numbers those add upto a target

# O(n) Time & Space
def solve_opt(arr, target):
    tracker = {}
    for i in range(len(arr)):
        diff = target - arr[i]
        if arr[i] in tracker:
            return (tracker[arr[i]], arr[i])
        else:
            tracker[diff] = arr[i]   
    return -1         

# O(n^2) Time and O(1) Space
def solve(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return -1            

if __name__ == "__main__":
    arr = [1,21,3,14,5,60,7,6]
    target = 82
    #print(solve(arr, target))
    print(solve_opt(arr, target))
