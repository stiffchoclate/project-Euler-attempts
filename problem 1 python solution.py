#purpose: sum of integers taht are multiplesof 3 and 5
#lead to general function for any two
#make a LCM function later

#brute force an answer (less efficeint)
#use  stabdard summation formulae
#puton  a 3d planre


m1 = int(input("m1: "))
m2 = int(input("m2: "))
limit = int(input("Upto: "))


def ssf_ans(m1,m2,limit):
    #step 1: find sum of m1 instances
    #step 2: find sum of  m2instances
    #step 3: find sum of (LCM) m1*m2instanbces
    #step 4: add m1, m2 instacnes and sub m1*m2 instances
    multiples = [m1,m2,m1*m2]
    sums = []
    for x in multiples:
        out = ("looking for sum of {0} multiples...").format(x)
        print(out)
        n = (limit-1)//x
        total = x*(n/2)*(n+1)
        sums.append(total)
        print(sums)
    ans = sums[0]+sums[1]-sums[2]
    out = ("""The sum of multiples of {0} and {1} from 0 to {2} is {3}.""").format(m1,m2,limit,ans)
    print(out)
ssf_ans(m1,m2,limit)
