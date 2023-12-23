# Task - Write a function called swap_values. This function takes a list of numbers and swaps the first element with the last element. For example,  if you pass [2, 4, 67, 7] as a argument, your function should return [7, 4, 67, 2]

def swap_values(nums):
    """This function receives a list and swaps the first and last element"""
    
    #check if object is a list
    if not isinstance(nums, list):
        # print(f"Object '{nums}' is not a list")
        raise TypeError(f"Object '{nums}' is not a list")
    #retrieve first and last element in the list
    first_v = nums[0]
    last_value = nums[-1]

    #make a copy of the list 
    nums_copy = nums[:]
    print(f"nums_copy = {nums_copy}")
    #swap new value in the copy list
    nums_copy[0] = last_value
    nums_copy[-1] = first_v

    #Print both list
    print(f"orginal list:", nums)
    print(f"modified list:", nums_copy)

swap_values(nums=[24, 6, 3, 5])
swap_values(nums=[2, 4, 67, 7])
swap_values(nums=1)