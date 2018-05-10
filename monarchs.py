monarchs = ['Louis XIV', 'Louis XVIII', 'Elizabeth II', 'Louis XIL', 'Christian IX']

numerals = {
	'I':1,
	'V':5,
	'X':10,
	'L':50
}

# Check if list is not null.
if monarchs:
	for monarch in monarchs:
		name, suffix = monarch.split(' ')
		order = 0
		if len(suffix) > 1:
			for i in range(1, len(suffix)):
				a = numerals[suffix[i-1]]
				b = numerals[suffix[i]]
				if a < b:
					order = order + b - a
				else:
					order = order + a
		else:
			order = numerals[suffix]
		print order
			
					
				
