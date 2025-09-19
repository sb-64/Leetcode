class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        slist = list(s)
        ls, cs = [], [] 
        
        for _ in range(len(slist)):
            for e in slist:
                if e not in cs:
                    cs += e
                else:
                    if len(ls) < len(cs):
                        ls = cs
                    slist.pop(0)
                    cs = []
                    break

        print(ls)
        return len(ls)


if __name__ == '__main__':
    sol = Solution()

    print(sol.lengthOfLongestSubstring('abcabcbb')) # abc, 3
    print(sol.lengthOfLongestSubstring('bbbbb')) # b, 1
    print(sol.lengthOfLongestSubstring('pwwkew')) # wke, 3
    print(sol.lengthOfLongestSubstring(' ')) # 1
    print(sol.lengthOfLongestSubstring('')) # 0

