class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(p)
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(m):
            if p[j] =='*':
                dp[j + 1][0] = dp[j - 1][0]
                matcher = p[j - 1]
                if matcher == '.':
                    for i in range(n):
                        dp[j + 1][i + 1] = dp[j - 1][i + 1] or dp[j][i] or dp[j+1][i]
                else:
                    for i in range(n):
                        dp[j + 1][i + 1] = dp[j - 1][i + 1] or ((dp[j][i] or dp[j+1][i]) and matcher == s[i])
            elif p[j] == '.':
                for i in range(n):
                    dp[j + 1][i + 1] = dp[j][i]
            else:
                for i in range(n):
                    dp[j + 1][i + 1] = dp[j][i] and p[j] == s[i]
        return dp[m][n]
