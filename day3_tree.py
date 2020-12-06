def tree(file):
	line=[]
	tree =0
	i=0
	line_number =0
	f = open(file, "r")	
	line.append(f.read())
	values=line[0].split("\n")
	for value in values:
		if value != values[-1]:
			print("i",i)
			line_number +=1
			if value[i] == "#":
				tree +=1
				print("tree=",tree)
			if  i+3 >len(value)-1:
				print("starting a new pattern from i =",i,line_number)
				i-=28
			else:
				i+=3	
		else:
		 	break

	print("Final tree total",tree)
		
tree("tree.txt")
