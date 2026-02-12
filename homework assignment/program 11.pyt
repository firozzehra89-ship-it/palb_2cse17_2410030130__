def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    max_reach = 0
    end_of_jump = 0
    jumps = 0

    for i in range(n - 1):
        max_reach = max(max_reach, i + arr[i])
        
        if i == end_of_jump:
            jumps += 1
            end_of_jump = max_reach
            
            if end_of_jump <= i:
                return -1
                
    return jumps

print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(min_jumps([1, 4, 3, 2, 6, 7]))
print(min_jumps([0, 10, 20]))
