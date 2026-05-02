'''

121
1231
12421
0

yes
no
yes

'''

def palindrome(n):
    length = len(n)

    for i in range(length//2):
        if n[i] != n[length - i - 1]:
            return "no"

    return "yes"



a = input()

while int(a):

    print(palindrome(a))

    a = input()