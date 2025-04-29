def knapsack(W, wt, val, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]

# Example
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
g = len(values)
print(" Knapsack Maximum Value:", knapsack(capacity, weights, values, g))
