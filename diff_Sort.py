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

# insertion_sort(nums)

def merge_sort(nums):
    if len(nums) > 1:
        left_nums = nums[:len(nums)//2]
        right_nums = nums[len(nums)//2:]
        
        # Recursion
        merge_sort(left_nums)
        merge_sort(right_nums)
        
        # merging
        i = 0 #left numsay index 
        j = 0 #right numsay index
        k = 0 #mergde numsay index
        while i < len(left_nums) and j < len(right_nums):
            if left_nums[i] < right_nums[j]:
                nums[k] = left_nums[i]
                i += 1
            else:
                nums[k] = right_nums[j]
                j += 1
            k += 1
         
        while i < len(left_nums):
            nums[k] = left_nums[i]
            i += 1
            k += 1

        while j < len(right_nums):
            nums[k] = right_nums[j]
            j += 1
            k += 1 

merge_sort(nums)
print(nums)

