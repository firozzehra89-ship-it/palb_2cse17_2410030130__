from collections import Counter

def is_subset(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    
    for val, count in count_b.items():
        if count_a[val] < count:
            return False
    return True

a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]
print(is_subset(a, b))
