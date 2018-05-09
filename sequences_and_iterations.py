## de bruijn ##
from pwn import *

pattern = cyclic(1024)
pattern_upper = cyclic(1024, alphabet=string.ascii_uppercase)
pattern_hex_lower = cyclic(alphabet='0123456789abcdef', n=4) # no length will generate the entire possibility space for length n
pattern_hex_upper = cyclic(alphabet='0123456789ABCDEF', n=4)

sub_index = cyclic_find('FF12', alphabet='0123456789ABCDEF', n=4) # locate part of pattern

context.cyclic_alphabet = '0123456789ABCDEF' # can set the alphabet globally for this instance

## itertools ##
from itertools import *

for char in cycle('xyz123'): # iterates endlessly over the provided alphabet
	pass
for permut in permutations('WXYZ', 2): # iterates over all combinations of `12345` with length 2
	pass
for item in starmap(some_func, tuple_list): # iterates over the results from calling some_func on each tuple in tuple_list
	pass
for i in ifilter(lambda x: x % 3 == 0, range(100)): # iterate over every number from 0-100 divisible by 3
	pass
islice(inf_iter, 5) # given some endless iterator (e.g. cycle, above), ends after 5 iterations
repeat(1, 337) # repeats 1 a total of 337 times
chain(some_array, some_tuple, some_iterable) # combine multiple collections into one
compress([1, 2, 3, 4], [True, False, False, True]) # return values from first array whose index in second array is True
