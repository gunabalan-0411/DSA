# DSA

## Tree
  - Tree	for top to bottom process, use logic before calling recursion and vice versa
  - For bottom to top process add additional return at end of the def
## Dynamic Programming - 1D
| Problem             | Hint                     | Note |
|---------------------|--------------------------|------|
| House robbing I  | dfs: max(dfs(i+1), nums[i]+dfs(i+2)), for dp: rob1, rob2 newRob = max(rob1+n, rob2), reassign alternative|      |
| House robbing II  | same but call it twice with 0 to -1, 1 to full |   to avoid circular issues   |



## Graph
| Problem             | Hint                     | Note |
|---------------------|--------------------------|------|
| Surrownded regions  | find land from 4 borders |      |

## Advanced Graph
| Problem             | Hint                     | Note |
|---------------------|--------------------------|------|
| Reconstruct itenarary | dfs to until each node ran out of adj vect by pop |      |


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
  - | Problem             | Hint                 | Note |
	|---------------------|----------------------|------|
	| Combination Sum   | append() and pop() compare total  |      |

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
```python
def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a
```
## Intervals
| Problem             | Hint                 | Note |
|---------------------|----------------------|------|
| eraseOverlapIntervals   | sort start and choose prevEnd with min end  |      |

## Bit Manipulation
  - Any number XOR (^) with same number gives 0 , 0 ^ n -> n
  - Any number AND (&) with 1 gives 1 OR 0 to calculate HammingWeight and further n>>=1
  ### Problems
    - Counting bits problem use offset (power of 2) and Dynamic programming: dp[i] = 1 + dp[i-offset]
  
