def password(file):
	line=[]
	counter = 0
	f = open(file, "r")	
	line.append(f.read())
	values=line[0].split("\n")
	for value in values:
		pw=value.split(" ")
		letter= pw[1][0]
		passw= pw[2]
		min,max = pw[0].split("-")
		#print(int(min),int(max))
		#print(passw.count(letter))
		if int(passw.count(letter)) >= int(min) and int(passw.count(letter)) <= int(max):
			counter +=1			
	print(counter)
		

password("input2.txt")