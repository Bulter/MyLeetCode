"""
    将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
    
    总结：
        1. 能想出构造二位矩阵然后填充，但是未考虑特殊情况（当行数或者列数为1时）；
        2. 进阶思路：构建二维矩阵 -> 压缩空间 -> 找到规律去掉二维矩阵
        3. from itertools import chain 中的chain(*list)函数，链子函数
"""


from itertools import chain


class Solution:
    def convert_ben(self, s: str, numRows: int) -> str:
        if len(s) < 2 or numRows == 1:
            return s
        
        columns = (len(s) // (numRows * 2 - 2) + 1) * (numRows - 1)
        char_list = [[""] * columns for _ in range(numRows)]

        n = 0
        for j in range(columns):
            for i in range(numRows):
                if not n < len(s):
                    break
                if j % (numRows - 1) == 0 or j % (numRows - 1) == (numRows - i - 1):
                    char_list[i][j] = s[n]
                    n += 1
        
        for i in char_list:
            print(i)
        
        return "".join(map(lambda x: "".join(x), char_list))
    
    def convert_yasuo(self, s: str, numRows: int) -> str:
        """
            考虑到二位矩阵中有大量空白，可以对矩阵进行压缩
            规律：每次都只对上一行的右侧添加
        """
        r = numRows
        if r < 2 or r >= len(s):
            return s
        
        # 找到行索引
        ri, t = 0, r * 2 - 2
        mat = [[] for _ in range(r)]
        for i, ch in enumerate(s):
            mat[ri].append(ch)
            ri += 1 if i % t < r - 1 else -1
            
        
        return "".join(chain(*mat))
    
    def convert_guilv(self, s: str, numRows: int) -> str:
        """
            找到每行对应原字符串s中下标的规律，这样可以去除列表，空间复杂度降为O(1)
            规律：
                0             0+t                    0+2t                     0+3t
                1      t-1    1+t            0+2t-1  1+2t            0+3t-1   1+3t
                2  t-2        2+t  0+2t-2            2+2t  0+3t-2             2+3t  
                3             3+t                    3+2t                     3+3t
        """
        n, r = len(s), numRows
        if r == 1 or r >= len(s):
            return s
        
        result = ""
        t = 2 * r - 2
        for i in range(r):
            for j in range(0, n - i, t):
                result += s[i+j]  # 当前周期第一个字符
                if 0 < i < r - 1 and j + t - i < n:
                    result += s[j+t-i]
        
        return result
            
        
    
    
if __name__ == "__main__":
    string = "PAYPALISHIRING"
    num = 4
    
    # string = "AB"
    # num = 1
    
    print(Solution().convert_yasuo(string, num))
                    
                    
                
        