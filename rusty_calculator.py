
string = '2*3*2'
digits = '0123456789'
operands = '+*'
newstring = []

newstring.append(string[0])
skip = False
for index in range(1,len(string)):
	#print 'Location:'
	#print index
	#print 'New String:'
	#print newstring
	if string[index] == '*' and not skip:
		#print 'Found asterix'
		next_digit = string[index+1]
		back_index = index - 1
		while newstring[back_index] == '*' and back_index>0:
			back_index = back_index - 1
		newstring.insert(back_index+1,next_digit)
		newstring.append('*')
		skip = True


	elif not skip:
		#print 'skipped'
		newstring.append(string[index])
	else:
		#print 'Reset skip'
		skip = False
	#print 'Status'
	#print newstring
print 'String:'
print string
print 'First pass:'
print ''.join(newstring)

popped = False
for index2 in range(1,len(string)):
	print 'Index2:'
	print index2
	print newstring
	if popped and newstring[index2] == '*':
		print 'Found asterix'
		
		if index2 == len(newstring)-1:
			newstring.append('+')
		else:
			newstring.insert[index2+1,'+']
			popped = False

	if newstring[index2] == '+' and not popped:
		print 'Popped'
		newstring.pop(index2)
		popped = True


print 'Second Pass:'
print ''.join(newstring)

# 2*2+2



