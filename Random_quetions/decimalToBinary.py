def dec_to_bin(n):
    ans = 0
    i = 0
    while n>0:
        rem = n%2
        ans += (10**i)*rem
        n = n//2
        i += 1
    
    return ans
n = 250
print(dec_to_bin(n))
