def selection_sort(nums):
    for i in range(0, len(nums)):
        min = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min]:
            # if nums[j] > nums[min]: Sort from big to small
                min = j
        print(nums)
        # nums[i], nums[min] = nums[min], nums[i]
        nums[min], nums[i] = nums[i], nums[min]
    print(nums)


selection_sort([51, 25, 65, 6, 78])