# Merging two sorted arrays into one.
# Used in Merge Sort
# O(n + m) Time & Space

def merge(arr1, arr2):
    i = j = 0
    output = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[j])
            j += 1

    if i < len(arr1):
        while i < len(arr1):
            output.append(arr1[i])
            i += 1

    if j < len(arr2):
        while j < len(arr2):
            output.append(arr2[j])
            j += 1        

    return output            

if __name__ == "__main__":
    a = [10,20,30,89,1000]
    b = [-1,-9,27,90,100]
    print(merge(a, b))