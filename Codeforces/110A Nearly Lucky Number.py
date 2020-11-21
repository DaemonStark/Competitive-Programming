def solve(n):
    ls = [4, 7]
    for each in str(n):
        if each not in str(ls):
            return False
        else:
            if len(str(n)) == 4 or len(str(n)) == 7:
                if each in str(ls):
                    return False
                else:
                    return True


if __name__ == '__main__':
    n = int(input())
    if(solve(n) == True):
        print("YES")
    else:
        print("NO")
