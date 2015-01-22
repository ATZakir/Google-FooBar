
def find_forward_total(sub_heights):
	forward_max = max(sub_heights)
	loc = sub_heights.index(forward_max)
	if len(sub_heights) < 2:
		return 0
	elif loc == 0:
		right_total = find_forward_total(sub_heights[1:])
		return right_total
	else:
		left_total = sub_heights[loc]*loc - sum(sub_heights[:loc])
		if loc + 1 == len(sub_heights):
			right_total = 0
		else:
			right_total = find_forward_total(sub_heights[loc+1:])
		return left_total + right_total

def find_backward_total(sub_heights):
	backward_max = max(sub_heights)
	loc = sub_heights.index(backward_max)
	length = len(sub_heights)
	if length < 2:
		return 0
	elif loc == length - 1:
		left_total = find_backward_total(sub_heights[:loc])
		return left_total
	else:
		right_total = sub_heights[loc]*(length - loc - 1) - sum(sub_heights[loc+1:])
		if loc == 0:
			left_total = 0
		else:
			left_total = find_backward_total(sub_heights[:loc])
		return left_total + right_total

def answer(heights):

	if len(heights) < 3:
		return 0

	loc = heights.index(max(heights))

	forward_total = find_forward_total(heights[loc+1:])
	backward_total = find_backward_total(heights[:loc])

	return forward_total + backward_total
