"""
Changes made:
1: removed max()
2: added in a static_n to check for the max revenue
3: added if statement to check if largest q is greater than p[static_n]
4: if q is larger than p[static_n] and n equals static n then print out combinations
*Notes*
If only a single printout appears above a length then that number will be added with itself.
If there are multiple printouts you must add two cuts together to get the correct length for max revenue.
As the price array gets longer the combinations will increase dramatically. To sift through the printouts
identify the max revenues that match and combine the cuts that equal to the length.
"""
import sys

p = (-1000, 1, 4, 7, 8, 10, 13, 14, 16, 20, 25, 28)


def CUT_ROD(p, n, stat_n):
    if n == 0:
        return 0
    q = -1000000
    for i in range(1, n+1):
        q = p[i] + CUT_ROD(p, n-i, stat_n)
        if q > p[stat_n] and n == stat_n:
            print("At length {} make a cut at {}'' at price {} for max revenue {}".format(n, i, p[i], q))
    return q


print("")
print("L = " + str(len(p)))

print("")
check = None
for i in range(1, len(p)):
    check = i
    sys.stdout.flush()
    print(str(i) + " (p="+str(p[i])+") => " + str(CUT_ROD(p, i, check)))