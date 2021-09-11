# Implement a function, findProduct(int arr[], int size) which takes an array arr and its size as an input and returns an array so that each index has a product of all the numbers present in the array except the number stored at that index.

# O(n) Time & O(n) Space
def solve_opt(arr):
    output = []
    total_prod = 1
    for i in range(len(arr)):
        total_prod *= arr[i]

    for i in range(len(arr)):
        prod = int(total_prod / arr[i])
        output.append(prod)
    return output    


# O(n^2) Time & O(n) Space 
def solve(arr):
    output = []
    for i in range(len(arr)):
        prod = 1
        for j in range(len(arr)):
            if j == i:
                continue
            prod *= arr[j]
        output.append(prod)
    return output        

if __name__ == "__main__":
    arr = [1,2,3,4,100]
    print(solve(arr))
    print(solve_opt(arr))
