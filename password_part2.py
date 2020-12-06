def password_part2(file):
	line=[]
	wrong = 0
	correct =0
	f = open(file, "r")	
	line.append(f.read())
	values=line[0].split("\n")
	for value in values:
		pw=value.split(" ")
		letter= pw[1][0]
		passw= pw[2]
		min,max = pw[0].split("-")		
		if (letter ==passw[int(min)-1] or letter ==passw[int(max)-1]) and not (letter ==passw[int(min)-1] and letter ==passw[int(max)-1]):
			correct +=1
	print("correct",correct)
		
password_part2("input2.txt")