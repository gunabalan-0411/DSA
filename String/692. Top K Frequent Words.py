from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # sort the list based on strings as per lexicographic sorting condition from question.
        words.sort()
        # counting the word occurence
        word_counts = {}
        for word in words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1

        return sorted(
            word_counts,
            key=lambda word: word_counts[word],
            reverse=True
        )[:k]
