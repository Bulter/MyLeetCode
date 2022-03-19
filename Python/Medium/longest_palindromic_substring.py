import time
from typing import Tuple


class Solution:
    def longest_palindrome_baoli(self, s: str) -> str:
        """
            暴力破解
        """
        begin = 0
        max_len = 1

        for i in range(len(s)):
            for j in range(i+2, len(s)+1):
                if j - i > max_len and self._is_palindrome(s[i:j]):
                    max_len = j - i
                    begin = i
        
        return s[begin:begin+max_len]

    def _is_palindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n):
            ri = n - i - 1
            if i >= ri:
                break
            if s[i] != s[ri]:
                return False
        return True
    
    def longest_palindrome_dp(self, s: str) -> str:
        """
            动态规划：
                穷举分析 -> 确定边界 -> 找到规律，确定最优子结构 -> 状态转移方程
        """
        n = len(s)
        
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        begin = 0    
        max_len = 1
        
        for l in range(2, n+1):  # 子字符串长度
            for i in range(n):  # 左边界索引
                ri = i + l - 1  # 右边界索引
                if ri > n-1:
                    break
                
                # 判断是否是回文字符串
                if s[i] == s[ri]:
                    if ri - i < 3:  # 如果在给定 s[i]==s[ri] 条件下 len(substring)<3 则肯定为回文字符串
                        dp[i][ri] = True
                    else:
                        dp[i][ri] = dp[i+1][ri-1]
                
                if dp[i][ri] and max_len < l:
                    max_len = l
                    begin = i
        
        return s[begin:begin+max_len]
    
    def longest_palindrome_center(self, s: str) -> str:
        begin = 0
        max_len = 1
        
        for i in range(len(s)):
            # 中心分两种，奇偶
            k, rk = self._expand_around_center(s, i, i)
            if rk - k + 1 > max_len:
                begin, max_len =k, rk - k + 1
            
            k, rk = self._expand_around_center(s, i, i+1)
            if rk - k + 1 > max_len:
                begin, max_len =k, rk - k + 1
        
        return s[begin:begin+max_len]
            

    def _expand_around_center(self, s: str, i: int, ri: int) -> Tuple[int]:
        while i >=0 and ri < len(s) and s[i] == s[ri]:
            i, ri = i - 1, ri + 1
        return i + 1, ri - 1
        
                    
                    
    

if __name__ == "__main__":
    string = "uwqrvqslistiezghcxaocjbhtktayupazvowjrgexqobeymperyxtfkchujjkeefmdngfabycqzlslocjqipkszmihaarekosdkwvsirzxpauzqgnftcuflzyqwftwdeizwjhloqwkhevfovqwyvwcrosexhflkcudycvuelvvqlbzxoajisqgwgzhioomucfmkmyaqufqggimzpvggdohgxheielsqucemxrkmmagozxhvxlwvtbbcegkvvdrgkqszgajebbobxnossfrafglxvryhvyfcibfkgpbsorqprfujfgbmbctsenvbzcvypcjubsnjrjvyznbswqawodghmigdwgijfytxbgpxreyevuprpztmjejkaqyhppchuuytkdsteroptkouuvmkvejfunmawyuezxvxlrjulzdikvhgxajohpzrshrnngesarimyopgqydcmsaciegqlpqnclpwcjqmhtmtwwtbkmtnntdllqbyyhfxsjyhugnjbebtxeljytoxvqvrxygmtogndrhlcmbmgiueliyfkkcuypvvzkomjrfhuhhnfbxeuvssvvllgukdolffukzwqaimxkngnjnmsbvwkajyxqntsqjkjqvwxnlxwjfiaofejtjcveqstqhdzgqistxwsgrovvwgorjaoosremqbzllgbgrwtqdggxnyvkivlcvnv"
    # string = 'babad'
    
    start_time = time.time()
    print(Solution().longest_palindrome_center(string))
    print(f"cost_time:{time.time() - start_time}s")
    
