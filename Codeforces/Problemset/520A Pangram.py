def pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s.lower():
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    s = str(input()[:n])
    if(pangram(s) == True):
        print("YES")
    else:
        print("NO")
