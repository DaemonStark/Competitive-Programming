# def Retype(N, K, S):
#     # Time already spent
#     time_already_spent = K - 1
#     total_time_to_complete = N
#     # Restart Condition
#     # add 1 min for restartig
#     # 1 min per level
#     restart_time = total_time_to_complete + 1
#     total_restart = time_already_spent + restart_time
#     # Move backward condition
#     # add 1 min per level
#     # add 1 for completing
#     going_back = K - S
#     remaining_levels = total_time_to_complete - S
#     complete_levels = remaining_levels + 1
#     total_backward = going_back + complete_levels + time_already_spent

#     # check which is less
#     if total_restart < total_backward:
#         return total_restart
#     else:
#         return total_backward


# if __name__ == "__main__":
#     t = int(input())
#     for i in range(1, t + 1):
#         N, K, S = map(int, input().split())
#         print("Case #{}: {}".format(i, Retype(N, K, S)))


T = int(input())

for cas in range(T):
    N, K, S = map(int, input().split(' '))
    print("Case #{}: {}".format(cas + 1, min(K + N, K + K - S + N - S)))
