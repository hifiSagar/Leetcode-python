class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        dp = [[0.0] * (i + 1) for i in range(101)]
        dp[0][0] = poured

        for i in range(query_row + 1):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    overflow = dp[i][j] - 1
                    dp[i][j] = 1
                    dp[i + 1][j] += overflow / 2.0
                    dp[i + 1][j + 1] += overflow / 2.0

        return min(1.0, dp[query_row][query_glass])
