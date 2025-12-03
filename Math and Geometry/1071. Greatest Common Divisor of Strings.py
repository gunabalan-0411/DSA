class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_1, len_2 = len(str1), len(str2)

        def isDivisor(l: int) -> bool:
            # checking if the substring can completely match with every characters
            # If there is remain which is left then its not a divisor
            if len_1 % l or len_2 % l:
                return False
            # Calculating the factor to multiple self whole occurance of the substring and compare it to the base strings
            f1, f2 = len_1 // l, len_2 // l

            return f1*str1[:l] == str1 and f2*str1[:l] == str2
        
        # looping from end so that we will start with big chunk of the smallest str as we process for GCD
        for l in range(min(len_1, len_2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ''