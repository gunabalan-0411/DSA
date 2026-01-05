# DSA

## Tree
  - Tree	for top to bottom process, use logic before calling recursion and vice versa
  - For bottom to top process add additional return at end of the def

## Trie
	```python
	class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

	class Trie:
	    def __init__(self, words):
	        self.root = TrieNode()
	        for word in words:
	            cur_node = self.root
	            for char in word:
	                if char not in cur_node.children:
	                    cur_node.children[char] = TrieNode()
	                cur_node = cur_node.children[char]
	            cur_node.is_word = True
	```
| Problem             | Hint                 | Note |
|---------------------|----------------------|------|
| Extra char in str   | res = 1 + dfs(i+1)   |      |

## Search
  - use set to search items using `in` keyword for fast retrieval

## BFS
  - BFS explores by increasing path length, so BFS algorithm itself gaurantee shortest path
  - to process invidividual items level by level use without for loop else use it to

## Backtrack
  - Subset problem: every iteration youll add and remove item with two recursive

## Heap
  - minheap	heapq.heapify(self.minHeap)
	- heapq.heappush(list, num)
  - heapq.heappop(list)
  - Use BFS + Min Heap	for min cost or max cost to reach certain position in graph

## String

  
## Math & Geometry
  ### Problems
    - GCD of Strings:
      - The modulas of the divisor with the items should not return remainder
    - Excel Sheet Column Title
      - O log 26 : from last digit calculate the offset (columnNumber - 1) % 26, to move from last move (columnNumber - 1) // 26

## Bit Manipulation
  - Any number XOR (^) with same number gives 0 , 0 ^ n -> n
  - Any number AND (&) with 1 gives 1 OR 0 to calculate HammingWeight and further n>>=1
  ### Problems
    - Counting bits problem use offset (power of 2) and Dynamic programming: dp[i] = 1 + dp[i-offset]
  
