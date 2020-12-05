def report_repair(file):
	s= set()
	numbers=[]
	f = open(file, "r")	
	numbers.append(f.read())
	list_of_numbers=numbers[0].split("\n")
	#print(list_of_numbers)
	for i in list_of_numbers:
		if (i !='  '):
			if (2020- int(i)) not in s:
				s.add(int(i))
			else:
				result = int(i) * (2020- int(i))
	#print(s)
	return(result)
report_repair("input1.txt")
