def solution(nums):
    kinds = len(set(nums))
    pick = len(nums) // 2
    return min(kinds, pick)
  