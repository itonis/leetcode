class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word2)
        n = len(word1)
        dp = list()
        dp = list(range(n + 1))
        for j, char2 in enumerate(word2):
            up = dp[0]
            dp[0] = j + 1
            for i, char1 in enumerate(word1):
                upleft = up
                up = dp[i + 1]
                if char1 == char2:
                    dp[i+1] = upleft
                else:
                    dp[i+1] = min([upleft, up, dp[i]]) + 1
        return dp[n]
