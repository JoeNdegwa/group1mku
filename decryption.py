import math

n = 143
phi = 120
e = 7
possible_keys = []
for integer in range(phi+1, phi+1000):
    if integer * e % phi == 1:
        possible_keys.append(integer)
        
        
print(possible_keys)
