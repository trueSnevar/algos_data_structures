# coding: utf-8
# successful submission: 73796188

def get_distance(str1: str, str2: str) -> int:
    n, m = len(str1), len(str2)

    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][m] = n - i
    for j in range(m + 1):
        dp[n][j] = m - j

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

    return dp[0][0]

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(get_distance(s1, s2))