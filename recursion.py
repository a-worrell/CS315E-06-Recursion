"""
Student information for this assignment:


Replace <FULL NAME> with your name.
On my honor, Audrey Worrell and, this
programming assignment is my own work and I have not provided this code to
any other student.


I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.


UT EID 1: ACW3428
UT EID 2:
"""




# TODO: Modify this function. You may delete this comment when you are done.
def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.


    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target == 0:
        return True
    if start >= len(nums):
        return False

    return (group_sum(start + 1, nums, target - nums[start]) or
            group_sum(start + 1, nums, target))






# TODO: Modify this function. You may delete this comment when you are done.
def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.


    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target == 0:
        return True
    if start >= len(nums):
        return False  

    if nums[start] == 6:
        return group_sum_6(start + 1, nums, target - nums[start])

    return (group_sum_6(start + 1, nums, target - nums[start]) or
            group_sum_6(start + 1, nums, target))

   
# TODO: Modify this function. You may delete this comment when you are done.
def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.


    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target == 0:
        return True
    if start >= len(nums):
        return False

    return (group_no_adj(start + 2, nums, target - nums[start]) or
            group_no_adj(start + 1, nums, target))


# TODO: Modify this function. You may delete this comment when you are done.
def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen


    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target == 0:
        return True
    if start >= len(nums):
        return False

    if nums[start] == 5:
        if start + 1 < len(nums) and nums[start + 1] == 1:
            return group_sum_5(start + 2, nums, target - nums[start])
        return group_sum_5(start + 1, nums, target - nums[start])

    return (group_sum_5(start + 1, nums, target - nums[start]) or
            group_sum_5(start + 1, nums, target))



# TODO: Modify this function. You may delete this comment when you are done.
def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.


    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target == 0:
        return True
    if start >= len(nums):
        return False

    clump_sum, next_index = nums[start], start + 1
    while next_index < len(nums) and nums[next_index] == nums[start]:
        clump_sum += nums[start]
        next_index += 1

    return (group_sum_clump(next_index, nums, target - clump_sum) or
            group_sum_clump(next_index, nums, target))


# TODO: Modify this function
def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function


    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    return split_array_helper(0, nums, 0, 0)

def split_array_helper(index, nums, sum1, sum2):
    if index >= len(nums):
        return sum1 == sum2
    return (split_array_helper(index + 1, nums, sum1 + nums[index], sum2) or
            split_array_helper(index + 1, nums, sum1, sum2 + nums[index]))

# TODO: Modify this function. You may delete this comment when you are done.
def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function


    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    return split_odd_10_helper(0, nums, 0, 0)

def split_odd_10_helper(index, nums, sum1, sum2):
    if index >= len(nums):
        return (sum1 % 10 == 0 and sum2 % 2 == 1) or (sum2 % 10 == 0 and sum1 % 2 == 1)
    return (split_odd_10_helper(index + 1, nums, sum1 + nums[index], sum2) or
            split_odd_10_helper(index + 1, nums, sum1, sum2 + nums[index]))

# TODO: Modify this function. You may delete this comment when you are done.
def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function


    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    return split_53_helper(0, nums, 0, 0)

def split_53_helper(index, nums, sum1, sum2):
    if index >= len(nums):
        return sum1 == sum2 and len(nums) > 0

    if nums[index] % 5 == 0:
        return split_53_helper(index + 1, nums, sum1 + nums[index], sum2)
    elif nums[index] % 3 == 0:
        return split_53_helper(index + 1, nums, sum1, sum2 + nums[index])

    return (split_53_helper(index + 1, nums, sum1 + nums[index], sum2) or
            split_53_helper(index + 1, nums, sum1, sum2 + nums[index]))

