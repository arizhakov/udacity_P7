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

# L3
print "L3:"
Nc = 6021. + 5e4
Xc  = 302. + 2.5e3
Ne = 5979. + 5e4
Xe = 374. + 2.5e3
pc = Xc/Nc
pe = Xe/Ne
ppool = (Xc+Xe)/(Nc+Ne)
SEpool = math.sqrt(ppool*(1.-ppool)*(1/Nc+1/Ne))
print pc
print pe 
print SEpool

diff = pc - pe
z = diff/SEpool
print z


# L5
print "L5:"
Xs_cont = [196, 200, 200, 216, 212, 185, 225, 187, 205, 211, 192, 196, 223, 192]
Ns_cont = [2029, 1991, 1951, 1985, 1973, 2021, 2041, 1980, 1951, 1988, 1977, 2019, 2035, 2007]
Xs_exp = [179, 208, 205, 175, 191, 291, 278, 216, 225, 207, 205, 200, 297, 299]
Ns_exp = [1971, 2009, 2049, 2015, 2027, 1979, 1959, 2020, 2049, 2012, 2023, 1981, 1965, 1993]



