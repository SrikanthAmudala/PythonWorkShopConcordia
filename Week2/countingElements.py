"""
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
"""
def countingElements(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i]+1 in arr:
            count+=1
    return count

arr = [1,1,2,2]
print(countingElements(arr))

