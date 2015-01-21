def digesting(eye, eye_minus):

	digest = ((129 * eye) ^ eye_minus) % 256

	return digest

def step(digest,prev_m,k):

	return ((digest+k*256) ^ prev_m) / 129

def answer(digest):

	message = []

	for index, d in enumerate(digest):
		print d
		if index == 0:
			message.append(step(d,0,0))
			continue

		for k in range(1000000):
			test_m = step(d,message[-1],k)
			if digesting(test_m,message[-1]) != d:
				continue
			message.append(test_m)
			break

	return message
