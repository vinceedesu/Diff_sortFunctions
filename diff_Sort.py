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
    print(nums)

 
#### Buble Sort #####
def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    
            print(nums)
        print(nums)
    
def insertion_sort(nums):
    for i in range(1,len(nums)):
        j = i
        while nums[j - 1 ] > nums[j] and j > 0:
            nums[j - 1], nums[j] = nums[j], nums[j-1]
            j -= 1
            
        print(nums)

insertion_sort(nums)


