from z3 import *

s = Solver()
v = [] 

# initial value can be 0, 1, or 53
v.append(Int('initial_value'))
s.add(v[0] == 0 | v[0] == 1 | v[0] == 53)

# some multipliers
v.append(Int('multiplier_1'))
s.add(v[1] >= 0)

v.append(Int('multiplier_2'))
s.add(v[2] >= 0)

# final constraint
s.add((v[0] + v[1] * 11 + v[2] * -1) == 1000)

# output solution
if s.check() == sat:
	m = s.model()
	for i in range(0, len(v)):	
		print(m[v[i]])