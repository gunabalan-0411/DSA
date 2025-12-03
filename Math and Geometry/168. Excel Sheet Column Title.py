class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        # it works exactly like numbers adding but instead of 0-9(10 Characters log 10) its A-Z (26 characters log 26)
        while columnNumber > 0:
            # Subtract -1 as we are starting from 1 for A not 0
            offset = (columnNumber-1) % 26
            # We are starting from end by finding the remainder
            res += chr(ord('A')+ offset)
            columnNumber = (columnNumber-1) // 26
        # As calucate and append it from end, so reversing before returning it
        return res[::-1]
        
        # Time Complexity O(log 26) -> O(logn) 