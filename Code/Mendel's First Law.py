
import os
os.chdir('C:/Users/yasha/Desktop/Python Programming/Rosalind/Data')

def probability_of_dom_allele(k,m,n):
    t = m + n + k
    # probability of dom allele given HH and HH:
    # (HH, HH), *(HH, Hh), *(HH,hh)
    p1 = (k/t) * ((k-1)/(t-1))
    p2 = 2 * ( ((k/t) * (m/(t-1))) + ((k/t) * (n/(t-1))) )
    p_HH = p1 + p2

    # probability of dom allele given Hh and Hh
    # (Hh, Hh)
    p_Hh = (3/4) * (m / t) * ((m-1) / (t - 1))

    # probability of dom allele given hh and Hh
    # *(hh, Hh)
    p_hh = (m / t) * (n / (t -1))
    print(p_HH, p_Hh, p_hh)

    return(p_HH + p_Hh + p_hh)

print(probability_of_dom_allele(20,18,20))