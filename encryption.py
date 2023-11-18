import math

n = 143
phi = 120
possible_keys = []
for integer in range(2,phi):
    if math.gcd(n,integer) == 1 and math.gcd(phi,integer) == 1:
        possible_keys.append(integer)
        
        
print(possible_keys)
