#Leet Code Question, Two Sum Solution
#Composed by Khali A. Crawford on 02/19/2023 @ 8:49 PM

#Instructions
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#My Solution
#Iterate througth the given array, adding each number to every other number one at a time until it equals the value of the target var
#grab the index of said numbers and return them

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: