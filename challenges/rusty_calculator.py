def answer(string):

	string = list(string)

	asterisk_count = 0
	index = 0

	while index < len(string):
		if string[index] == "*":
			string.pop(index)
			asterisk_count+=1
		elif string[index] == '+' and asterisk_count > 0:
			for replace in range(asterisk_count):
				string.insert(index,'*')
			index+=asterisk_count
			asterisk_count = 0
		else:
			index+=1

	if asterisk_count > 0:
		for replace in range(asterisk_count):
			string.insert(index,'*')


	plus_count = 0
	index2 = 0

	while index2 < len(string):
		if string[index2] == '+':
			string.pop(index2)
			plus_count+=1
		else:
			index2+=1

	if plus_count > 0:
		for replace in range(plus_count):
			string.insert(index2,'+')


	return ''.join(string)


