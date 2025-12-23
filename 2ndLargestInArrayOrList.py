#Second Largest Number in a List

#arr = list(map(int, input().split()))
arr = [1, 9, 5, 2, 3]

largest = second = float('-inf')

for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x < largest:
        second = x

print(second)
