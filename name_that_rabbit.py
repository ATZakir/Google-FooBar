from operator import itemgetter


def get_value(name,values):

	total = 0
	for char in name:
		total+=values[char]
	return total

def answer(names):

	values = {}
	letters = list('abcdefghijklmnopqrstuvwxyz')

	for index in range(26):
		values[letters[index]] = index + 1
	
	name_tupes = []
	for name in names:
		name_tupes.append((name,get_value(name,values)))
	
	name_tupes = sorted(name_tupes, key=itemgetter(1,0), reverse=True)

	return [name[0] for name in name_tupes]
