# Egyptian Fraction Representation of 2/3 is 1/2 + 1/6
# Egyptian Fraction Representation of 6/14 is 1/3 + 1/11 + 1/231
# Egyptian Fraction Representation of 12/13 is 1/2 + 1/3 + 1/12 + 1/156

# GeeksForGeeks link:
# https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/



import math
def egyptian_fraction(n,d):
    print("The Egyptian Fraction"+f"Reptresentaion of {n}/{d}",end="\n")
    eg_fr = []
    while n != 0:
        x = math.ceil(d/n)
        eg_fr.append(x)
        n = x * n - d
        d = d * x
    for i in range(len(eg_fr)):
        if i != len(eg_fr) - 1:
            print(f"1/{eg_fr[i]} +",end=" ")
        else:
            print(f"1/{eg_fr[i]}",end=" ")
egyptian_fraction(6,14)
        