
def split_array(tosplit):
	size = len(tosplit) / 2
	return tosplit[:size], tosplit[size:]

def binary_search(possible_values, test_func, test_single=False):
	if (len(possible_values) == 1):
		if (test_single and test_func(possible_values)):
			return possible_values[0]
		elif (not test_single):
			return None
	elif (len(possible_values) == 0):
		return None

	test, fail = split_array(possible_values)
	if (test_func(test)):
		return binary_search(test, test_func, test_single)
	else:
		return binary_search(fail, test_func, test_single)


## example ##
def test(values):
	buf = ','.join(values)
	send_line(buf)
	return "success" in read_lines_until()

binary_search(all_possible_values, test)