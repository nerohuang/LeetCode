s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"


s1Index = 0;
s2Index = 0;
s3Index = 0;

while s1Index < len(s1) or s2Index < len(s2):
    if s1Index < len(s1) and s1[s1Index] == s3[s3Index]:
        s1Index += 1
        s3Index += 1
    elif s2Index < len(s2) and s2[s2Index] == s3[s3Index]:
        s2Index += 1
        s3Index += 1
    else:
        print(False)