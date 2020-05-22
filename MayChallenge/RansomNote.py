"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineCounter = {}
        for i in magazine:
            if magazineCounter.get(i) == None:
                magazineCounter[i] = 1
            else:
                magazineCounter[i] += 1

        for i in ransomNote:
            if magazineCounter.get(i) == None or magazineCounter.get(i) == 0:
                return False
            else:
                magazineCounter[i] -= 1
        return True

