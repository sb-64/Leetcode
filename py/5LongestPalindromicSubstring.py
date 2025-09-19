
class Solution:
    def longestPalindrome(self, s: str) -> str:

        str_len: int = len(s)
        ls: str = ''
        
        # create two pointers, where left is always right.
        for left in range(str_len):
            for right in range(str_len, left, -1):
                substr = s[left: right]

                # must be palindromic AND must be longer than what we have as the longest.
                if substr == substr[::-1] and len(substr) > len(ls): ls = substr

        return ls

            




        

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('babad')) # bab
    print(sol.longestPalindrome('cbbd')) # bb
