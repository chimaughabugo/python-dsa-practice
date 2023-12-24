# Task - Write a function called swap_values. This function takes a list of numbers and swaps the first element with the last element. For example,  if you pass [2, 4, 67, 7] as a argument, your function should return [7, 4, 67, 2]

def swap_values(nums: list[any]):
    """ This swaps the first and last elements of the list using simultaneous assignment"""
    nums[0], nums[-1] = nums[-1], nums[0]
    return nums