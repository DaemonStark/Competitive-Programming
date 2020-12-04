t = int(input())
for i in range(0, t):
    n, m = map(int, input().split())
    n_list = []
    m_list = []
    n_list = [int(item) for item in input().split()]
    m_list = [int(item) for item in input().split()]
    print(len(set(n_list) & set(m_list)))
