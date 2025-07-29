class Solution:
    def countAndSay(self, n: int) -> str:
        res, counter = '1', 0
        
        while counter < n:
            print("res: " + res)
            for i in res:
                l, r = 0, len(res) - 1
                c = 1
                while l < r and res[l] == res[l+1]:
                    c += 1
                    print(f"C: " + c)
                    l += 1
                res = str(c) + str(i) 
            counter += 1
        return res
        
S = Solution()
print(S.countAndSay(1))