#REVERSE INTEGER : LEETCODE
#def reverse_integer(x):
#    sign = -1 if x < 0 else 1
#    x = abs(x)
#
#    rev = 0
#
#    while x > 0:
#        digit = x % 10
#        rev = rev * 10 + digit
#        x //= 10
#
#    rev *= sign
#
#    if rev < -2**31 or rev > 2**31 - 1:
#        return 0
#
#    return rev
#
#x = int(input("Enter an integer: "))
#print("Reversed:", reverse_integer(x))


##GFG: If-else
#
#n, m = map(int, input("Enter values of n and m: ").split())
#
#if n<m:
#    print("lesser")
#elif n>m:
#    print("greater")
#elif n == m:
#    print("equal")




