list = [5, 2, 3, 4, 1]
print("Original List:", list)

sum = 0
for num in list:
    sum += num
print("Sum of all elements in the list:", sum)

average = sum / len(list)
print("Average of all elements in the list:", average)

list.sort()
print("Sorted List:", list)

print("Minimum item in the list:", list[0])
print("Maximum item in the list:", list[-1])