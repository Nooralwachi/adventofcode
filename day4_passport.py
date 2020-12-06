def passport(file):
	line_number =0
	line=[]
	valid=0
	needed_fields=['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
	f = open(file, "r")	
	line.append(f.read())
	values=line[0].split("\n\n")
	#print(values)
	for value in values:
		
		line_number +=1
		print("line_number:",line_number)
		available =needed_fields[:]
		pp =(" ").join(value.split("\n"))
		#print("pp:",pp)
		fields =pp.split(" ")
		#print("fields:",fields)
		for x in fields:
			#print(x[0:3])
			if x[0:3] in available:
				print(available)
				available.remove(x[0:3])
		if len(available)>0 :
			if available[0]=='cid':
				print("pass")
				valid+=1
			else:
				print("NOT pass")
		else:
			print("pass")
			valid+=1
	print(valid)


passport("passport.txt")