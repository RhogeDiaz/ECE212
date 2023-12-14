def containsDuplicate(nums):
    checker = []
    is_in = 0
    for i in range(0, len(nums)):
        print()
        for j in range(0, len(nums)):
            print(is_in)
            if nums[i] in checker:
                is_in += 1
        checker.append(nums[i])
    if is_in != 0:
        return True
    else:
        return False

nums = [1,2,3,1]
print(containsDuplicate(nums))