"""
    给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 1:
            return 0
                
        rk = 1
        k = max_n = 0
        s_set = set(s[0])
        
        while n-k > max_n:
            
            # 判断是否重复
            while rk < n and (not s[rk] in s_set):
                s_set.add(s[rk])
                # 右指针往右
                rk += 1
            
            max_n = max(len(s_set), max_n)
            s_set.remove(s[k])
            # 左指针往右
            k += 1
            
        return max_n

    def lengthOfLongestSubstring_new(self, s: str) -> int:
        k, max_n = -1, 0
        s_dict =dict()
        
        for i, c in enumerate(s):
            
            # 此处更新左边界为什么需要 s_dict[c] > k 的原因：
            #     如字符串 tmmzuxt 中，t第一次出现时 {t:0}, k=-1 ，
            #     在m第二次出现时更新左边界，此时 {t:0, m:1}, k=1 ，
            #     在t第二次出现时，此时 s_dict[t]=0, k=1 ，
            #     子字符串 mzuxt中并没有重复，并不需要更新左边界，
            #     如果不进行限制进行更新左边界则获取错误答案。
            if c in s_dict and s_dict[c] > k:
                k = s_dict[c]
            else:
                max_n = max(max_n, i - k)
            s_dict[c] = i
            
            print(f"i:{i}, k:{k}, max_n:{max_n}, s_dict:{s_dict}")

        return max_n


if __name__ == "__main__":
    s = "tmmzuxt"
    # print(Solution().lengthOfLongestSubstring(s))
    print(Solution().lengthOfLongestSubstring_new(s))
        