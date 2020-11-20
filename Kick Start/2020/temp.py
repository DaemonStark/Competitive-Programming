def solve(num):
    if num == 0:
        return 0
    s = list(map(int, str(num)))
    l = len(s)
    ans = (5 ** l - 5) // 4
    odd = True
    for i in range(l):
        cur = s[i]
        curodd = (s[i] % 2 == 1)
        start = 1 if odd else 0
        count = 0
        while start < cur:
            count += 1
            start += 2
        ans += count * 5 ** (l - i - 1)
        if odd != curodd:
            return ans
        odd = not odd
    return ans + 1


T = int(input())

for cas in range(T):
    L, R = map(int, input().split(' '))
    print("Case #{}: {}".format(cas + 1, solve(R) - solve(L - 1)))
