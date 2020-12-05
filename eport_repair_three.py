def report_repair(file, value):
	s= set()
	numbers=[]
	f = open(file, "r")	
	numbers.append(f.read())
	list_of_numbers=numbers[0].split("\n")
	#print(list_of_numbers)
	for i in list_of_numbers:
		if (i !='  '):
			if (value- int(i)) not in s:
				s.add(int(i))
			else:
				x= [int(i),value- int(i)]
				return x

def report_repair_three(file):
	s= set()
	numbers=[]
	f = open(file, "r")	
	numbers.append(f.read())
	list_of_numbers=numbers[0].split("\n")
	for i in list_of_numbers:
		if (i !='  '):
			x=report_repair("input1.txt",(2020- int(i)))
			if x is not None:
				result= x[0]*x[1]*int(i)
				return result
			elif int(i) not in s:
				s.add(int(i))

print(report_repair_three("input1.txt"))
