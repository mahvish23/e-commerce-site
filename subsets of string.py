"""" Input : abc
Output : a, b, c, ab, bc, ac, abc

Input : aaa
Output : a, aa, aaa
"""
def printsubsets(s,c,i):
    if i==len(s):

        if len(c)==0:
            print([""])
            return
        print(c)
        return
    printsubsets(s,c,i+1)
    printsubsets(s,c+s[i],i+1)
s=input()
printsubsets(s,"",0)

