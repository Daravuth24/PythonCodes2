def b_search(nums_list, sno):
    while True:
        beg = 0
        end = len(nums_list)-1
        mid = (beg + end) // 2

        if nums_list[mid] == sno:
            return mid
        elif nums_list[mid] > sno:
            end = mid-1
        else:
            beg = mid+1
    else:
        return -1

pos = b_search([50,65,78,98,99,100], 78)
print(f"The element found at {pos}")