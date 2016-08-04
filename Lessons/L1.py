import math
import scipy.stats as st
#st.norm.ppf(.95)
#>>>1.6448536269514722

N = 2000.
x  = 300.
conf_level = 0.99
z_score = st.norm.ppf(conf_level + (1-conf_level)/2)
#print z_score

p = x/N
print N*p
print N*(1-p)

m = z_score * (math.sqrt(p*(1-p)/N))
print m
print p-m
print p+m


