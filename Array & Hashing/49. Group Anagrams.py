from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap to store the grouping
        word_groups = defaultdict(list)
        # iterate the list of strs:
        for word in strs:
            # store char counts
            char_counts = [0] * 26
            for char in word:
                char_counts[ord(char)-ord('a')] += 1
            # changing the data type from list to tuple to use this as key
            # because the tuples are unhashable meaning we can't change the value 
            word_groups[tuple(char_counts)].append(word)
        return list(word_groups.values())