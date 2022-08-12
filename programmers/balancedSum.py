# input: [1, 4, 2, 5]
# output: 2
# Explanation: if 2 is the partition, subarrays are [1, 4] and [5]

# input: [2, 3, 4, 1, 4, 5]
# output: 1
# Explanation: if 1 is the partition, subarrays are [2, 3, 4] and [4, 5]

# input: [1, 2, 3]
# output: -1
# Explanation: No subarrays possible. return -1

def balancedSum(arr):
    lsum = 0
    rsum = sum(arr) - arr[0]
    for i in range (1, len(arr) - 1):
        lsum += arr[i - 1]
        rsum -= arr[i]
        if lsum == rsum:
            return i
    return 0