#Python Lists

# Find largest & smallest number

#arr = list(map(int, input("Enter the elements: ").split()))
#
#largest = arr[0]
#smallest = arr[0]
#
#for i in range(len(arr)):
#    if arr[i] > largest:
#        largest = arr[i]
#    if arr[i] < smallest:
#        smallest = arr[i]
#
#print("Largest:", largest)
#print("Smallest:", smallest)

## Find and remove duplicates
#
#arr = list(map(int, input("Enter the elements: ").split()))
#
#unique = []
#
#for num in arr:
#    if num not in unique:
#        unique.append(num)
#
#print(unique)

#Reverse a List

#arr = list(map(int, input("Enter the list elements: ").split()))
#print(arr[::-1])
#
## OR
#
#arr = list(map(int, input("Enter the list elements: ").split()))
#
#n = len(arr)
#
#for i in range(n // 2):
#    temp = arr[i]
#    arr[i] = arr[n - i - 1]
#    arr[n - i - 1] = temp
#
#print(arr)

# second largest number in a list

arr = list(map(int, input("Enter the list elements: ").split()))

# Step 1: find the largest
largest = arr[0]
for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

# Step 2: find the largest number smaller than 'largest'
second_largest = None
for i in range(len(arr)):
    if arr[i] != largest:
        if second_largest is None or arr[i] > second_largest:
            second_largest = arr[i]

# Step 3: output result
if second_largest is None:
    print("No second largest element")
else:
    print("Second Largest:", second_largest)

















    





