def countSubStr(s, n) :  
    a = 0
    b = 0  
    for i in range(n) :
        if (s[i : i + 4] == "kick") : 
            a += 1  
  
        if (s[i :i+ 5] == "start") : 
            b = b + a  
    return b  

if __name__ == "__main__" :  
    t = int(input())
    for i in range(1, t + 1):
        s = input().lower()
        n = len(s)
        print("Case #{}: {}".format(i, countSubStr(s, n)))