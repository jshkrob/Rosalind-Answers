def rabbit_pairs(n, k):
    # base case:
    if n == 1 or n == 2:
        return(1)
    else:
        return(k * rabbit_pairs(n-2,k) + rabbit_pairs(n-1,k))

def rabbit_pairs_(n,k):
    prev1,prev2 = 1,1
    for i in range(2, n):
        prev1, prev2 = prev2, k*prev2 + prev1
    return(prev2)

print(rabbit_pairs(31,2))