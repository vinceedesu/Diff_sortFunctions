# Pls also do the tutorial for the ff algorithm:
# Selection Sort
# Bubble Sort
# Insertion Sort
# Merge Sort
# Quick Sort

# Selection Sort

nums = [80, 68, 10, 31, 85, 67, 53, 100, 82, 19]

def selection_sort(nums):
    
    for i in range(9):
        minPosition = i
        for j in range(i,10):
            if nums[j] < nums[minPosition]:
                minPosition = j
    
        temp = nums[i]
        nums[i] = nums[minPosition]
        nums[minPosition] = temp
    
        print(nums)


# nums = [80, 68, 10, 31, 85, 67, 53, 100, 82, 19]
selection_sort(nums)
print(nums)