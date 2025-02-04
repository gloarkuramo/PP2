def permute(s, s2):
    if len(s) == 0:
        print(s2)
        return
    
    for i in range(len(s)):
        char = s[i]
        left_s = s[0:i]
        right_s = s[i+1:]
        rest = left_s + right_s
        permute(rest, s2 + char)

s1 = (input())
s2 = ""
permute(s1, s2)
